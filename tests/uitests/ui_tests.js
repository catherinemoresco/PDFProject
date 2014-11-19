// container value to hold test pass-fail strings 
var testResults = "";

function testOutput(num, isPassed) {
  return "Test " + num ": " + (isPassed ? "Passed" : "Failed") + "\n":
}

function test(num, isPassed) {
  testResults += testOutput(num, isPassed);
}

//test 1: Upload Button
test(1, uploadButtonTest());

//Test 2: Correct File Type
test(2, !setUFile("test.jpg"));

//Test 3: Correct File Type
test(3, setUFile("test.pdf"));

//Test 4: Proper Highlighting 
test(4, !setHRectangle(-100, -100, 0, 0));

//Test 5: Proper Highlighting 
test(5, !setHRectangle(6000, 6000, 7000, 7000));

//Test 6: Proper Highlighting 
test(6, !setHRectangle(0,0,0,0));

//Test 7: Proper Highlighting
var l = getLine(1);
test(7, setHRectangle(l[0], l[1], l[2], l[3])
          && compareHRectangle(l[0],l[1],1[2],l[3]));

//Test 8: Proper Highlighting
test(8, setHRectangle(l[0]-10,l[1],1[2]+10,l[3])
    && compareHRectangle(l[0],l[1],1[2],l[3]));

//Test 9: Proper Highlighting
test(9, setHRectangle(ll[0]-10,l[1]-4,1[2]+10,l[3]-4)
    && compareHRectangle(l[0],l[1],1[2],l[3]));

//Test 10: Proper Highlighting
var j = getLine(3);
test(10, setHRectangle(j[0],j[1],j[2],j[3])
    && !compareHRectangle(l[0],l[1],1[2],l[3]));
//There are other cases in this category I'd like to implement but these require already having analyzed a pdf file

//Test 11: Proper annotating 
test(11, !setARectangle(-100,-100,0,0,"lkdvnjanvlfanlfna"));

//Test 12: Proper annotating 
test(12, !setARectangle(6000,6000,7000,7000,"assdvafb"));

//Test 13: Proper annotating 
test(13, !setARectangle(0,0,0,0,"snddddddddddddddddddddddn"));

//Test 14: Proper annotating 
test(14, setARectangle(50,50,100,100,""));
test(13, setARectangle(50,50,100,100,"hello world")); // FIXME

//Test 15: Proper annotating 
test(15, setARectangle(300,50,400,100,"HELLO")
    && compareARectangle(300,50,400,100,"HELLO"));

//Test 16: Proper annotating 
test(16, setARectangle(50,50,100,100,"HELLO")
    && compareARectangle(50,50,100,100,"HELLO"));

//Test 17: Proper annotating 
test(17, setARectangle(50,50,100,100,"HELLO") 
    && !compareARectangle(50,50,100,100,""));
