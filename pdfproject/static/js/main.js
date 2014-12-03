// get JSON data
	var jsonArray
	var jpath = "/static"+window.location.pathname+'.json.txt'; 
	function getData(jpath){
		jsonArray = $.getJSON( jpath, function() {
			console.log( "success" );
		})
		.done(function() {
			console.log( "second success" );
		})
		.fail(function() {
			console.log( "error" );
		});
	}

	getData(jpath)



// a line is fully highlighted if the selection
// area spans its entire height, and the x-coordinates
// overlap
	function fullHighlight(selectionBox, lineBox){
		if ((lineBox[0][1] > selectionBox[0][1]) && (lineBox[1][1] < selectionBox[1][1])){
			if (!(selectionBox[0][0] > lineBox[1][0] || lineBox[0][0] > selectionBox[1][0])){
				return true;
			}
		}
		return false;
	}

// checks if two rectangles intersect
	function intersectRect(r1, r2){
		if ((r1[0][0] > r2[1][0]) || (r2[0][0]) > r1[1][0]){
			return false;
		}
		if ((r1[1][1] < r2[0][1]) || (r2[1][1]) < r1[0][1]){
			return false;
		}
		return true; 
	}


		var  divs = document.getElementsByClassName('pdf-page');
		var divLen = divs.length;
		var divDraws= [];
		var pageGroups = []
		var initX,initY,mousedown,dynamicRect, highlightGroup;
		var currHighlightID = 0;
		var scalingFactor;
		var imagePath = [];
		var followLines = true;
		var accentColor = '#D98C3C';



	// create divs
		for(var i=0;i<divLen;i++){
			divID = divs[i].id;
			divDraws[i] = SVG(divID);
			var image_item = new Array();
			var fpath = '/'+divs[i].id;
			imagePath[i] = fpath;
			var image = divDraws[i].image(fpath);
			divID = i;
			divs[i].id = divID;
			scale(image,divs[i]);
			pageGroups[i] = divDraws[i].group().opacity(0.5);

			// event listeners on divs to create highlights

			divs[i].addEventListener("mousedown",function(event){
				if(event.button == 0){
					initX = event.pageX-this.offsetLeft-this.offsetParent.offsetLeft;
					initY= event.pageY-this.offsetTop-this.offsetParent.offsetTop;
					mousedown = true;
				}
			})
			
			divs[i].addEventListener("mousemove",function(){
				if (mousedown === true){
					if (!(highlightGroup)){
						highlightGroup = pageGroups[eval(this.id)].group().id(currHighlightID);
						currHighlightID++;
					}
					var endX = event.pageX-this.offsetLeft-this.offsetParent.offsetLeft;
					var endY= event.pageY-this.offsetTop-this.offsetParent.offsetTop;

					// iterate through page lines to draw highlights
					if (followLines){

					var pageRects = jsonArray.responseJSON[+this.id + 1]

						for (var line in pageRects){
							if (pageRects.hasOwnProperty(line)){
								deleteHighlight(line, highlightGroup, i);
								makeHighlight(pageRects[line], initX, endX, initY, endY, line, highlightGroup, i);
							}
						}
					}

					else{
						deleteSimpleHighlight(highlightGroup, i);
						makeSimpleHighlight(initX, endX, initY, endY, highlightGroup, i)

					}
				}
			})
			
			divs[i].addEventListener("mouseup",function(event){
				mousedown = false;			

				if(highlightGroup){
						highlightGroup = false;
					}
		
			})
		}

	// set highlight mode; default is lines
	$(".svg-button.lines").bind("click", function(){
		$(".svg-button.lines > svg").css({fill: accentColor});
		$(".svg-button.nolines > svg").css({fill: '#ffffff'});
		followLines = true;
	})

	$(".svg-button.nolines").bind("click", function(){
		$(".svg-button.nolines > svg").css({fill: accentColor});
		$(".svg-button.lines > svg").css({fill: '#ffffff'});
		followLines = false;
	})

	function makeSimpleHighlight(initX, endX, initY, endY,highlightGroup, currentDiv){
		var rect = highlightGroup.rect(Math.max(endX-initX, 0), Math.max(endY-initY,0)).move(initX, initY).fill('#FFFF66').id(currentDiv + "g" + highlightGroup).attr("fullHighlight", true);
		rect.on("dblclick", function(){this.parent.remove()})
	};

	function makeHighlight(line, initX, endX, initY, endY, lineid, highlightGroup, currentDiv){
		var pointOne = scalepoint(line[0])
		pointOne[0] -= 25;
		pointOne[1] -= 5;

		var pointTwo = scalepoint(line[1])
		pointTwo[0] += 25;
		pointTwo[1] += 5;

		// fully highlight lines
		if (fullHighlight([[initX, initY],[endX, endY]], [pointOne, pointTwo])){
			var rect = highlightGroup.rect(Math.max(pointTwo[0]-pointOne[0]),Math.max(pointTwo[1] - pointOne[1], 0)).move(pointOne[0], pointOne[1]).fill('#FFFF66').id(currentDiv + "g" + highlightGroup + "line" + lineid).attr("fullHighlight", true)

			rect.on("dblclick", function(){this.parent.remove()})
			return rect;
			}
		// draw partial highlights on lines that are not fully highlighted
		else if (intersectRect([[initX, initY],[endX, endY]], [pointOne, pointTwo])){
			var startHighlight, endHighlight;
			if (initY < pointOne[1]){
				startHighlight = pointOne[0];
			}
			else{
				startHighlight =Math.max(pointOne[0], initX);
			}
			if (endY > pointTwo[1]){
				endHighlight = pointTwo[0];
			}
			else{
			 endHighlight = (pointTwo[0], Math.min(endX, pointTwo[0]));
			}
			var rect = highlightGroup.rect(Math.max(endHighlight-startHighlight, 0), Math.max(pointTwo[1] - pointOne[1], 0)).move(startHighlight, pointOne[1]).fill('#FFFF66').id(currentDiv + "g" + highlightGroup + "line" + lineid).attr("fullHighlight", false);
			return rect;
			}
			return false;
		};


		// delete a highlight on doubleclick
		function deleteHighlight(lineid, highlightGroup, currentDiv){
			var highlight = document.getElementById(currentDiv + "g" + highlightGroup + "line" + lineid);
			if (!!highlight){
					highlight.remove();
			}
		}

		function deleteSimpleHighlight(highlightGroup, currentDiv){
			var highlight = document.getElementById(currentDiv + "g" + highlightGroup);
			if (!!highlight){
					highlight.remove();
			}
		}

	// adjust point by a scaling factor, where a point is represented as a tuple
		function scalepoint(point){
			return [point[0] * scalingFactor, point[1]*scalingFactor];
		}

		function scale (img,divElem){
			//var w =window.innerWidth;
			var w =1024;
			divElem.style.width = (w + "px");
			img.loaded(function(loader){
				var h = (1/loader.ratio)*w;
				scalingFactor = w/loader.width;
				img.size(w,h);
				divElem.style.height = (h + "px");
			})		
		}
		// Input: a string of the form "#ffc8b0"
		// Output: A list of RGB components as integers, of the form [255, 200, 176]
		function hexstring_to_numlist(fillColor) {
			var c = [fillColor.substring(1,3), fillColor.substring(3,5), fillColor.substring(5,7)];
			c = c.map(function(component){ return parseInt(component,16) });
			return c;
		}
		/**
 		* Convert an image 
 		* to a base64 string
 		* @param  {String}   url         
 		* @param  {Function} callback    
 		* @param  {String}   [outputFormat=image/png]           
		* http://stackoverflow.com/questions/6150289/how-to-convert-image-into-base64-string-using-javascript?lq=1
 		*/
		function convertImgToBase64(url, callback, outputFormat){
    		var canvas = document.createElement('CANVAS'),
        		ctx = canvas.getContext('2d'),
        		img = new Image;
    		img.crossOrigin = 'Anonymous';
    		img.onload = function(){
        		var dataURL;
        		canvas.height = img.height;
        		canvas.width = img.width;
        		ctx.drawImage(img, 0, 0);
        		dataURL = canvas.toDataURL(outputFormat);
        		callback.call(this, dataURL);
        		canvas = null; 
    		};
    		img.src = url;
		}
		function px_to_mm(px) {
			var DPI = 120;
			return px;
			return (px*25.4)/DPI;
		}
		function px_to_ppts(px, page_px_measurement, page_inch_measurement) {
			PPI = 72;
			return px / page_px_measurement * PPI * page_inch_measurement;
		}
/*		// https://stackoverflow.com/questions/22172604/convert-image-url-to-base64
		// Usage: var base64 = getBase64Image($("#imageid"));
		function getBase64Image(img) {
			var canvas = document.createElement("canvas");
			canvas.width = img.width;
			canvas.height = img.height;
			var ctx = canvas.getContext("2d");
			ctx.drawImage(img, 0, 0);
			var dataURL = canvas.toDataURL("image/jpg");
			return dataURL.replace(/^data:image\/(png|jpg);base64,/, "");
		}
*/

		function export_to_pdf(method) {
			method = typeof method !== 'undefined' ? method : "saveas";

			// Create a new PDFKit document to hold our annotations
			var doc = new PDFDocument({layout: 'portrait', size: [72*8.5, 72*11.0]});
			stream = doc.pipe(blobStream());

			var k, pg;
			for(pg = 0; pg < divDraws.length; pg++) { // for each page in the document
				page_px_width = $('svg image')[pg].width.baseVal.value;
				page_px_height = $('svg image')[pg].height.baseVal.value;
				page_inch_width = 8.5;
				page_inch_height = 11;

				// rects = rect elements on the current page of the PDF document
				rects = $($('.pdf-page svg')[pg]).find('rect');
				//console.log(rects);
				rect_list = []; // list of rects we need to draw in the PDF

				rects.each(function(ix,el){
					var rect_list_item = new Array();
					rect_list_item["pos_x"] = px_to_ppts( $(this).attr('x'), page_px_width, page_inch_width );
					rect_list_item["pos_y"] = px_to_ppts( $(this).attr('y'), page_px_height, page_inch_height );
					rect_list_item["width"] = px_to_ppts( $(this).attr('width'), page_px_width, page_inch_width );
					rect_list_item["height"] = px_to_ppts( $(this).attr('height'), page_px_height, page_inch_height );
					rect_list_item["fillColor"] = $(this).attr('fill');
					rect_list_item["fillColor_decimal"] = hexstring_to_numlist(rect_list_item["fillColor"]);
					if( !!$(this).attr('opacity') )
						rect_list_item["opacity"] = parseInt( $(this).attr('opacity') );
					if(!rect_list_item["opacity"] && !!$(this).css('opacity') )
						rect_list_item["opacity"] = parseInt( $(this).css('opacity') );
					rect_list.push(rect_list_item);
					//console.log("Opacity of rect:");
					//console.log(rect_list_item["opacity"]);
				});
				//console.log("rect_list is now:");
				//console.log(rect_list);

				// Import the current document (as JPEG) as the base layer of the exported file.
				//pageimage = $($('.pdf-page svg')[pg]).find('image');
				pageimageURL = imagePath[pg];
				console.log(pageimageURL);
				pageimageWidth = parseInt(divs[pg].style.width.split('p')[0]);
				pageimageHeight = parseInt(divs[pg].style.height.split('p')[0]);
				pageimageX = 0;
				pageimageY = 0;
				console.log("Width " + pageimageWidth + "\nHeight " + pageimageHeight + "\n(x,y) " + pageimageX + "," + pageimageY);
				//doc.image(pageimageURL, pageimageX, pageimageY);
//				doc.image(new Buffer(image.replace('data:image/jpg;base64,',''), 'base64'), pageimageX, pageimageY);

convertImgToBase64(pageimageURL, function(img){
	doc.image(new Buffer(img.replace('data:image/jpg;base64,',''), 'base64'), pageimageX, pageimageY);
}, "image/jpg");

				// Draw each rectangular highlight.
				for(k = 0; k < rect_list.length; k++) {
					console.log("drawing a rect"); console.log(rect_list[k]);
					doc.rect(rect_list[k]["pos_x"], rect_list[k]["pos_y"], rect_list[k]["width"], rect_list[k]["height"])
						.fillOpacity(rect_list[k]["opacity"])
						.fill(rect_list[k]["fillColor"]);
				} // for each rectangle

				// Add a new page in the generated PDF
				if(pg >= divDraws.length-1) {
					doc.addPage();
				}

			} // for each page

			doc.end();
			stream.on('finish', function(){
				if(method == 'window') {
					url = stream.toBlobURL('application/pdf');
					window.location = url;
				}
				else if(method == 'saveas') {
					saveAs(stream.toBlob(), "export.pdf");
				}
			});
		} // function export_to_pdf
