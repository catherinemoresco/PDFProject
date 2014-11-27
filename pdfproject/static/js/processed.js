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
			lineDiv.style.height = (h+"px");
			lineDiv.style.width = (w+"px");
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
		lineDraws[i][j] = SVG(lineDivs[i][j].id);
		lineDraws[i][j].on('resize',function(){
			console.log(this.parent);
			var k = this.parent.id.split(':')[0];
			var w = this.parent.style.width.split('p')[0] * newWindowWidth[k-1]/oldWindowWidth[k-1];
			var h = this.parent.style.height.split('p')[0] * newWindowWidth[k-1]/oldWindowWidth[k-1];
			var x = this.parent.style.left.split('p')[0] * newWindowWidth[k-1]/oldWindowWidth[k-1];
			var y = this.parent.style.top.split('p')[0] * newWindowWidth[k-1]/oldWindowWidth[k-1];
			//console.log( 'k: '+ k + ' w: '+ w +' h: '+ h +' x: '+ x+' y: '+ y); 
			this.parent.style.width = (w*1.04+"px");
			this.parent.style.height = (h + "px");
			this.parent.style.left = (x -10+ "px");
			this.parent.style.top = (y + -10+"px");
			this.size('100%','100%');
		});
		lineDraws[i][j].fire('resize');
		lineDraws[i][j].rect('100%','100%').fill('#FFFF66').opacity('0.5')
	}
}