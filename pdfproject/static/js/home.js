function validateForm(){
	var up = document.getElementById("choose-file").value || false;
	if (up){
		var patt = /\.(pdf|PDF)$/; 
		var result = patt.test(up);
		if(!result){
			alert("Invalid File: Not a PDF");
			return false;
		}
		return true;
	}
	alert("Invalid File: No file specified");
	return false;
}	