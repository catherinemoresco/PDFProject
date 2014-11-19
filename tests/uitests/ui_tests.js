var j, l;

var testResults = "";

function test(num, expect, actual, descriptor) { // TODO: use descriptor
  var testResult, testDiagnosis;

  testResult = expect == actual ? "Passed" : "Failed";
  testDiagnosis = "Test " + num ": " + testResult + "\n";

  testResults += testDiagnosis;
}

test(1, uploadButtonTest(), true, "Upload button works");

// Test correct file types
test(2, setUFile("test.jpg"), false, "setUFile() does not take .jpg");
test(3, setUFile("test.pdf"), true, "setUFile() takes .pdf");

//Test 4: Proper Highlighting 
test(4, setHRectangle(-100, -100, 0, 0), false, 
    "setHRectangle does not take negative arguments");

//Test 5: Proper Highlighting 
test(5, setHRectangle(6000, 6000, 7000, 7000), false,
    "setHRectangle arguments cannot be abnormally large");
// FIXME: better descriptor

//Test 6: Proper Highlighting 
test(6, setHRectangle(0,0,0,0), false,
    "setHRectangle does not take dimension of 0");

//Test 7: Proper Highlighting
l = getLine(1);
test(7, setHRectangle(l[0], l[1], l[2], l[3])
          && compareHRectangle(l[0],l[1],1[2],l[3]), true,
     "setHRectangle works");

//Test 8: Proper Highlighting
l = getLine(1);
test(8, setHRectangle(l[0]-10,l[1],1[2]+10,l[3])
    && compareHRectangle(l[0],l[1],1[2],l[3]), true,
     "setHRectangle works");

//Test 9: Proper Highlighting
l = getLine(1);
test(9, setHRectangle(l[0]-10,l[1]-4,1[2]+10,l[3]-4)
    && compareHRectangle(l[0],l[1],1[2],l[3]), true,
     "setHRectangle works");

//Test 10: Proper Highlighting
j = getLine(3);
test(10, setHRectangle(j[0],j[1],j[2],j[3])
    && !compareHRectangle(l[0],l[1],1[2],l[3]), true,
     "setHRectangle works");
//There are other cases in this category I'd like to implement but these require already having analyzed a pdf file

//Test 11: Proper annotating 
test(11, setARectangle(-100,-100,0,0,"lkdvnjanvlfanlfna"), false,
    "setARectangle does not take negative dimensions");

//Test 12: Proper annotating 
test(12, setARectangle(6000,6000,7000,7000,"assdvafb"), false,
    "setARectangle does not take abnormally large dimensions");

//Test 13: Proper annotating 
test(13, setARectangle(0,0,0,0,"snddddddddddddddddddddddn"), false,
    "setARectangle does not take value 0 dimensions");

//Test 14: Proper annotating 
test(14, setARectangle(50,50,100,100,""), true,
    "setARectangle() accepts the empty string");
test(13, setARectangle(50, 50, 100, 100, "hello world"), true,
    "setARectangle() accepts general string input"); // FIXME

//Test 15: Proper annotating 
test(15, setARectangle(300,50,400,100,"HELLO")
    && compareARectangle(300,50,400,100,"HELLO"), true,
    "setARectangle() works");

//Test 16: Proper annotating 
test(16, setARectangle(50,50,100,100,"HELLO")
    && compareARectangle(50,50,100,100,"HELLO"), true,
    "setARectangle() works");

//Test 17: Proper annotating 
test(17, setARectangle(50,50,100,100,"HELLO") 
    && !compareARectangle(50,50,100,100,""), true,
    "setARectangle() works");
