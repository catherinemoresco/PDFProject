		var  divs = document.getElementsByClassName('pdf-page');
		var divLen = divs.length;
		var divDraws= [];
		var initX,initY,mousedown,dynamicRect;
		for(var i=0;i<divLen;i++){
			divID = divs[i].id;
			divDraws[i] = SVG(divID);
			var fpath = '/'+divs[i].id;
			var image = divDraws[i].image(fpath);
			divID = i;
			divs[i].id = divID;
			scale(image,divs[i]);
			divs[i].addEventListener("mousedown",function(event){
				if(event.button == 0){
					initX = event.pageX-this.offsetLeft-this.offsetParent.offsetLeft;
					initY= event.pageY-this.offsetTop-this.offsetParent.offsetTop;
					//alert("X: "+initX+" Y: "+initY);
					mousedown = true;
					console.log(this.offsetTop);
				}
			})
			
			divs[i].addEventListener("mousemove",function(){
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

			})
			
			divs[i].addEventListener("mouseup",function(event){
				if(dynamicRect){
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
					
				}			
			})
		}
		function scale (img,divElem){
			//var w =window.innerWidth;
			var w =1024;
			divElem.style.width = (w + "px");
			img.loaded(function(loader){
				var h = (1/loader.ratio)*w;
				img.size(w,h);
				divElem.style.height = (h + "px");
			})		
		}

