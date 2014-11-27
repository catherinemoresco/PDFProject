var initX,initY,mousedown,dynamicRect;
var winRatio,imgRatio;
var divDraws= [];
var divLines = [];
var divLineDraws = [];

function initSVG(divs){
	var divLen = divs.length;
	for(var i=0;i<divLen;i++){
		divID = divs[i].id;
		divDraws[i] = SVG(divID);
		var fpath = '/'+divs[i].id;
		var image = divDraws[i].image(fpath);
		divID = i;
		divs[i].id = divID;
		
		//ADDING EVENT LISTENER FOR IMAGES
		SVG.registerEvent('resize');
		image.on('resize',function(){
			//console.log(this.parent);
			var w =window.innerWidth *0.95;
			this.parent.parent.style.width = (w + "px");
			this.loaded(function(loader){
				imgRatio = loader.ratio;
				winRatio = w/loader.width;
				console.log(imgRatio);
				var h = (1/loader.ratio)*w;
				this.size(w,h);
				this.parent.parent.style.height = (h + "px");
			});
		});
		image.fire('resize');
		divLines[i] = divs[i].getElementsByClassName('line');
		var divLinesLen = divLines[i].length;
		//console.log(divLines[i]);
		divLineDraws[i] = [];
		for( var j = 0; j<divLinesLen;j++){
			divLineDraws[i][j] =SVG(divLines[i][j].id);
			divLineDraws[i][j].on('resize', function(){
				var w = (this.parent.style.width.split('p')[0] * winRatio);
				var h = (1/imgRatio)*w;
				//this.size(w,h);
				this.parent.style.width = (w+"px");
				this.parent.style.height = (h + "px");
				
				var x = (this.parent.style.left.split('p')[0] * winRatio);
				console.log(imgRatio);
				this.parent.style.left = x +'px';
				//var y = (this.parent.

			})
			divLineDraws[i][j].fire('resize');
		}
		
		//scale(image,divs[i]);
		
		
		// divs[i].addEventListener("mousedown",function(event){
			// if(event.button == 0){
				// initX = event.pageX-this.offsetLeft-this.offsetParent.offsetLeft;
				// initY= event.pageY-this.offsetTop-this.offsetParent.offsetTop;
				// //alert("X: "+initX+" Y: "+initY);
				// mousedown = true;
				// // console.log(this.offsetTop);
			// }
		// });
		
		
/* 		divs[i].addEventListener("mousemove",function(){
			if(mousedown){
				var endX = event.pageX-this.offsetLeft-this.offsetParent.offsetLeft;
				var endY= event.pageY-this.offsetTop-this.offsetParent.offsetTop;
				if(endX<initX || endY<initY){
					mousedown =false;
					return true;
				}
				if(dynamicRect){
					dynamicRect.width(endX-initX).height(endY-initY)
				}
				else{
					dynamicRect = divDraws[eval(this.id)].rect(endX-initX,endY-initY).move(initX,initY).fill('#FFFF66').opacity('0.5');
				}
			}
	
		}) */
		
	//	divs[i].addEventListener("mouseup",function(event){
/* 			if(dynamicRect){
				dynamicRect.remove();
				dynamicRect = false;
			}	
			if(mousedown){
				mousedown = false;			
				var endX = event.pageX-this.offsetLeft-this.offsetParent.offsetLeft;
				var endY= event.pageY-this.offsetTop-this.offsetParent.offsetTop;
				var rect = divDraws[eval(this.id)].rect(endX-initX,endY-initY).move(initX,initY).fill('#FFFF66').opacity('0.5');
				rect.dblclick(function(){
					this.remove();
				})
			}			 */
	//	});
		
	}
}