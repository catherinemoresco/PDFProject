function validateForm(){
  var up = document.getElementById("uploadFile").value;
  var patt = /\.(pdf|PDF)$/; 

  var result = patt.test(up);

  if(!result){
    alert("Invalid File");
    return false;
  }
  return true;
}	
