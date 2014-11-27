//Global Variables
//JSON
var jpath = "/static"+window.location.pathname+'.json.txt'; 
var jsonArray; 
//Div Element arrays
var  pageDivs = document.getElementsByClassName('pdf-page');
var  lineDivs = [];
//SVG Arrays
var pageDraws = [];
var lineDraws= [];
// Resize ratio arrays
var newWindowWidth = [];
var oldWindowWidth = [];
var imgRatio = [];
//Mouse Variables
var initX,initY;
var currX,currY;
var mousedown;
//Dynamically Drawn Rectangles
var dynamicRects;
//On Window Load Get JSON Data
window.onload = getData();

//Function Gets JSON Data And Then Calls makeLineDivs. This is necessary because of asynchronous execution
function getData(){
	jsonArray = $.getJSON( jpath, function() {
		console.log( "success" );
	})
	.done(function() {
		console.log( "second success" );
		makeLineDivs();
	})
	.fail(function() {
		console.log( "error" );
	});
}
//Function create line divs from JSON data and then calls loadImages.
function makeLineDivs(){
	$.each(jsonArray.responseJSON, function(index,value){
		$.each(value, function(index2,value2){
			var topX= value2[0][0];
			var topY= value2[0][1];
			var bottomX = value2[1][0];
			var bottomY = value2[1][1];
			var w = (bottomX-topX);
			var h = (bottomY-topY);
			lineDiv = document.createElement("div");
			lineDiv.className ='line';
			lineDiv.id = index+':'+index2;
			lineDiv.style.position ='absolute';
			lineDiv.style.top = (topY +"px");
			lineDiv.style.left = (topX+"px");
			lineDiv.style.height = (h*1.04+"px");
			lineDiv.style.width = (w*1.04+"px");
			//console.log(lineDiv);
			pageDivs[index-1].appendChild(lineDiv);
			//console.log("page: "+ index + " line: "+index2+ " box "+value2[0] + value2[1]);
		});
	});
	loadImages();
}
//Load pdf page images and attach event listeners that will handle auto resize. This will call loadLines.
function loadImages(){
	var pages  = pageDivs.length;
	for(var i=0;i<pages;i++){
		//create SVG container that will render page
		pageDraws[i] = SVG(pageDivs[i].id);
		var imgPath = '/' +pageDivs[i].id;
		//rename parent for easier array access
		pageDivs[i].id =i;
		var image = pageDraws[i].image(imgPath);
		//Create resize event listener
		SVG.registerEvent('resize');
		image.on('resize', function(loader){
			var w = window.innerWidth;
			oldWindowWidth[this.parent.parent.id] = newWindowWidth[this.parent.parent.id];
			newWindowWidth[this.parent.parent.id] = w;
			var h = (1/imgRatio[this.parent.parent.id])*w;
			this.size(w,h);
			this.parent.parent.style.width = (w+'px');
			this.parent.parent.style.height = (h+'px');
		});
		//Create Mouse Events
		pageDivs[i].addEventListener("mousedown",function(event){
			if(event.button == 0){
				initX = event.pageX-this.offsetLeft-this.offsetParent.offsetLeft;
				initY= event.pageY-this.offsetTop-this.offsetParent.offsetTop;
				mousedown = true;
				dynamicRects = [];
				//console.log('X: '+initX+' Y: '+initY);
			}
		});
		pageDivs[i].addEventListener("mousemove",function(event){
			if(mousedown == true){
				currX = event.pageX-this.offsetLeft-this.offsetParent.offsetLeft;
				currY= event.pageY-this.offsetTop-this.offsetParent.offsetTop;
				console.log(mousedown);
			}
		});
		pageDivs[i].addEventListener("mouseup",function(event){
			if(event.button == 0){
				endX = event.pageX-this.offsetLeft-this.offsetParent.offsetLeft;
				endY= event.pageY-this.offsetTop-this.offsetParent.offsetTop;
				mousedown = false;
				//console.log('X: '+endX+' Y: '+endY);
			}
		});
/* 		pageDivs[i].addEventListener("mouseout",function(event){
			if(mousedown == true){
				var numRects = dynamicRects.length;
				for(var k = 0;k<numRects;k++){
					dynamicRects[i].remove();
				}
				mousedown = false;
			}
		}); */

		//Wait for image to load and then move on to create making lines
		image.loaded(function(loader){
			newWindowWidth[this.parent.parent.id] = loader.width;
			imgRatio[this.parent.parent.id] = loader.ratio;
			this.fire('resize');
			loadLines(this.parent.parent.id);
		});
	}
}
function loadLines(i){
	lineDivs[i] = pageDivs[i].getElementsByClassName('line');
	var lines = lineDivs[i].length;
	lineDraws[i] =[];
	for(var j =0; j<lines;j++){
		lineDivs[i][j].id = i+':'+j;
		lineDraws[i][j] = SVG(lineDivs[i][j].id);
		
		lineDraws[i][j].on('resize',function(){
			//console.log(this.parent);
			var k = this.parent.id.split(':')[0];
			var w = this.parent.style.width.split('p')[0] * newWindowWidth[k]/oldWindowWidth[k];
			var h = this.parent.style.height.split('p')[0] * newWindowWidth[k]/oldWindowWidth[k];
			var x = this.parent.style.left.split('p')[0] * newWindowWidth[k]/oldWindowWidth[k];
			var y = this.parent.style.top.split('p')[0] * newWindowWidth[k]/oldWindowWidth[k];
			//console.log( 'k: '+ k + ' w: '+ w +' h: '+ h +' x: '+ x+' y: '+ y); 
			this.parent.style.width = (w+"px");
			this.parent.style.height = (h + "px");
			this.parent.style.left = (x -10+ "px");
			this.parent.style.top = (y + -10+"px");
			this.size('100%','100%');
		});
		lineDraws[i][j].fire('resize');
		//lineDraws[i][j].rect('100%','100%').fill('#FFFF66').opacity('0.5');
		//Add Mouse events to lineDivs
		lineDivs[i][j].addEventListener("mouseover",function(event){
				if(mousedown == true){

					if(initY < this.style.top.split('p')[0] || initX <this.style.left.split('p')[0]){
						var k = this.id.split(':')[0];
						var l = this.id.split(':')[1];
						var x = this.style.left.split('p')[0];
						var w = currX - this.offsetLeft-this.offsetParent.offsetLeft - x;
						var rect = lineDraws[k][l].rect('100%',w).move(0,0).fill('#FFFF66').opacity('0.1');
						rect.dblclick(function(){
							this.remove();
						})
					} 
/* 					else{
						mousedown = false;
						var numRects = dynamicRects.length;
						for(var k = 0;k<numRects;k++){
							dynamicRects[i].remove();
						}
					}	 */
				}
		});
 		lineDivs[i][j].addEventListener("mousemove",function(event){
				if(mousedown == true){
					var k = this.id.split(':')[0];
					var l = this.id.split(':')[1];
					var w = currX - lineDraws[k][l].last().x() ;
					lineDraws[k][l].last().width(w);
				}
		});
		lineDivs[i][j].addEventListener("mouseout",function(event){
				if(mousedown == true){
					var k = this.id.split(':')[0];
					var l = this.id.split(':')[1];
					if(currY > this.style.bottom.split('p')[0] || currX >this.style.right.split('p')[0]){
						lineDraws[k][l].last().size('100%','100%');
					}
					else{
						lineDraws[k][l].last().size(0,0);
					}
				}
		});
		 
	}
}