function makeDivs(divs){
	//GET JSON DATA
	var jpath = "/static"+window.location.pathname+'.json.txt';
	var jsonArray = $.getJSON( jpath, function() {
		console.log( "success" );
	})
	.done(function() {
		console.log( "second success" );
		getData(divs,jsonArray);
	})
	.fail(function() {
		console.log( "error" );
	});
}
function getData(divs,arr){
	//console.log(arr.responseJSON)
	$.each(arr.responseJSON, function(index,value){
		$.each(value, function(index2,value2){
			var topX= value2[0][0];
			var topY= value2[0][1];
			var bottomX = value2[1][0];
			var bottomY = value2[1][1];
			var w = bottomX-topX;
			var h = bottomY-topY;
			lineDiv = document.createElement("div");
			lineDiv.className ='line';
			lineDiv.id = index+':'+index2;
			lineDiv.style.position ='absolute';
			lineDiv.style.top = (topY +"px");
			lineDiv.style.left = (topX+"px");
			lineDiv.style.height = (h+"px");
			lineDiv.style.width = (w+"px");
			//console.log(lineDiv);
			divs[index-1].appendChild(lineDiv);
			//console.log("page: "+ index + " line: "+index2+ " box "+value2[0] + value2[1]);
		});
	});
	initSVG(divs);
}