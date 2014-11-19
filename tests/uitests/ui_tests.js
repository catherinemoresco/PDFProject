// container value to hold test pass-fail strings 
var m = ""

function testOutput(num, isPassed) {
  return "Test " + num ": " + (isPassed ? "Passed" : "Failed") + "\n":
}

//test 1: Upload Button
m += testOutput(1, uploadButtonTest());

//Test 2: Correct File Type
m += testOutput(2, setUFile("test.jpg") == false);

//Test 3: Correct File Type
m += testOutput(3, setUFile("test.pdf") == true);

//Test 4: Proper Highlighting 
m += testOutput(4, setHRectangle(-100, -100, 0, 0) == false);

//Test 5: Proper Highlighting 
m += testOutput(5, setHRectangle(6000, 6000, 7000, 7000) == false);

//Test 6: Proper Highlighting 
m += testOutput(6, setHRectangle(0,0,0,0) == false);

//Test 7: Proper Highlighting
var l = getLine(1);
m += testOutput(7, setHRectangle(l[0],l[1],1[2],l[3])
    && compareHRectangle(l[0],l[1],1[2],l[3]));

//Test 8: Proper Highlighting
m += testOutput(8, setHRectangle(l[0]-10,l[1],1[2]+10,l[3])
    && compareHRectangle(l[0],l[1],1[2],l[3]));

//Test 9: Proper Highlighting
m += testOutput(9, setHRectangle(ll[0]-10,l[1]-4,1[2]+10,l[3]-4)
    && compareHRectangle(l[0],l[1],1[2],l[3]));

//Test 10: Proper Highlighting
var j = getLine(3);
if(setHRectangle(j[0],j[1],j[2],j[3]) == true){
  if(compareHRectangle(l[0],l[1],1[2],l[3]) == false){
    m = m + " Test 9: passed\n";
  }
  else{
    m = m + " Test 9: Failed\n";
  }
}
else{
  m = m + " Test 9: Failed\n";
}
//There are other cases in this category I'd like to implement but these require already having analyzed a pdf file

//Test 11: Proper annotating 
if(setARectangle(-100,-100,0,0,"lkdvnjanvlfanlfna") == false){
  m = m + " Test 11: Passed\n";
}
else{
  m = m + " Test 11: Failed\n";
}

//Test 12: Proper annotating 
if(setARectangle(6000,6000,7000,7000,"assdvafb"); == false){
  m = m + " Test 12: Passed\n";
}
else{
  m = m + " Test 12: Failed\n";
}

//Test 13: Proper annotating 
if(setARectangle(0,0,0,0,"snddddddddddddddddddddddn") == false){
  m = m + " Test 13: Passed\n";
}
else{
  m = m + " Test 13: Failed\n";
}

//Test 14: Proper annotating 
if(setARectangle(50,50,100,100,"") == true){
  m = m + " Test 14: Passed\n";
}
else{
  m = m + " Test 14: Failed\n";
}
if(setARectangle(50,50,100,100,"hello world") == true){
  m = m + " Test 13: Passed\n";
}
else{
  m = m + " Test 13: Failed\n";
}

//Test 15: Proper annotating 
if(setARectangle(300,50,400,100,"HELLO") == true){
  if(compareARectangle(300,50,400,100,"HELLO") == true){
    m = m + " Test 14: passed\n";
  }
  else{
    m = m + " Test 14: Failed\n";
  }
}
else{
  m = m + " Test 14: Failed\n";
}

//Test 16: Proper annotating 
if(setARectangle(50,50,100,100,"HELLO") == true){
  if(compareARectangle(50,50,100,100,"HELLO") == true){
    m = m + " Test 16: passed\n";
  }
  else{
    m = m + " Test 16: Failed\n";
  }
}
else{
  m = m + " Test 14: Failed\n";
}

//Test 17: Proper annotating 
if(setARectangle(50,50,100,100,"HELLO") == true){
  if(compareARectangle(50,50,100,100,"") == false){
    m = m + " Test 16: passed\n";
  }
  else{
    m = m + " Test 16: Failed\n";
  }
}
else{
  m = m + " Test 14: Failed\n";
}
