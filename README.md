# The PDF Project 

*For Software Construction Fall 2014*

Catherine Moresco, Jonathan Jin, Megan Barnes, Michael Zhao, Alberto Rios, and Cristian Saucedo

## Update 11/19/14: Iteration 2 Plans
Features to be included:

##### UI:
- Highlights!
- Annotations!
- Deleting highlights and annotations!
- Some fine-looking front-end desgin!

##### Server:
- Modified PDF document download!
	+ Getting highlight data from frontend
	+ Merging highlights and SVG edits
- Streamlined file handling!

##### Image processing:
- Refined image processing algorithms!
	 + Better skew detection accuracy
	 + Enhanced handling of noise and blacked-out margins
- Eliminate ImageMagick dependency!
	+ Require Ghostscript instead, which has a much simpler installation process.

##### Overall: 
- Opportunities for user correction of algorithmic failings!

## Features

Features successfully implemented in this iteration include:
- File uploading
- Exporting PDF pages to JPG images
- Image processing
	+ Skew detection and correction
	+ Extraction of text line coordinates
- Image display

## Example Usage and Recommended Acceptance Tests
It's pretty simple to use: upload your own document with the "upload" button, and watch it appear---processed and straightened!

The best images are ones that are well formed, and have only one page of text per PDF page. Images imbedded in the text are OK!


## Dependencies
Install python packages with `pip install -r <path/to/requirements.txt>`.

Third party packages (see respective websites for installation instructions):

- [OpenCV2](http://opencv.org/)
- [Ghostscript](http://ghostscript.com/doc/current/Install.htm)

## How to Run
After installing dependencies, you can run the app locally with `python runserver.py`.

For automatic server-crash recovery, install supervisord and start the server using `run.sh`.

## How to Run Unit Tests
#####Image Processing Tests:
From within tests/cvtests, run the command `python -m unittest -v cv_unit_tests`.

The folder 'cvtests' contains the test file and copies of source files for our image processing algorithms.  More specific information about which functions and what functionality the tests are concerned with is within 'cv_unit_tests.py'.

*- Megan and Catherine*

##### UI Tests:
 The unit tests that we initially submitted will not run given the changes in our UI desgin.We are researching automated processes for testing UI that will be incorporated into Iteration 2.

 1. Run the app locally with `python runserver.py`
 2. Run the individual test suites with `python tests/uitests/<suite_name>`

 *- Alberto and Cristian*

#### Program Structure (Step-by-step)
1. Our web app contains the initial functionality for uploading a PDF.  The app's code can be found in pdfproject/__init__.py, with functions to handle the home screen, as well as uploading.  The content/styling/javascript functions for the app's pages can be found within pdfproject/templates and pdfproject/static.
2. Once the user has chosen a PDF to upload, the upload_file() function in __init__.py saves the file to the uploads folder on the server
3. upload_file() then calls processing.process() from pdfproject/processing.py on the PDF file to initialize image processing
	a. process() first calls extract.extractImages() from pdfproject/extract.py in order to pull images (.jpg) representing each page of the PDF from the file.  These will be passed to the rest of the image processing functions.
	b. process() calls skew.straighten() (from pdfproject/skew.py) on each of the images, which first uses skew.horizontal_sums() to help calculate the probable skew angle of the input image and then skew.rotate() to generate an image rotated at that angle.  It returns a rotated image for every input image.
	c. process() calls getlines.getLines() on each straightened image.  getLines() calls its helper function, getlines.isolateLines() which contains the entire algorithm for creating a grayscale image which has black where blank space should be and white where it thinks there are text lines.  getLines() then detects the pixel coordinates of the lines and returns them in a list.
4. processing.process() gathers the lines and puts them in a dictionary, mapped to their page number as a key.  The dictionary is returned as a json string.
5. Passing the json string back to the web app as a ....json.txt file, upload_file() in __init__.py redirects to a page which corresponds to the uploaded_file() function in __init__.py, which displays each of the processed images that were returned after straightening and reads the line coordinates for highlighting from the ....json.txt file.  The page is once again rendered using html/css/javascript from pdfproject/templates and pdfproject/static.
6. THE REST OF THIS NEEDS TO BE ABOUT RENDERING HIGHLIGHTS/ANNOTATIONS AND SAVING/EXPORTING FILES WHEN IT IS POSSIBLE.  PLEASE REVIEW/CORRECT/ADD STUFF


## Who did What
### Alberto & Cristian: 
We were in charge of User Interface design. We created the HTML displayed, worked on uploading files to server, passing files to CV modules, and displaying the resulting files.

### Catherine & Megan: 
We were in charge of the Computer Vision aspect of the project, which had several challenging aspects.

##### PDF Rasterizing
We put a lot of research into pre-existing PDF rendering software; while PDF itself is not a proprietary format, PDF documents cannot be rasterized for image processing with any software written in pure Python. We began with a Python library that provides Python bindings for the ImageMagick software suite. 

PythonMagick has several downsides: 
- It is incredibly difficult to install.
- It is slow. 
- It is virtually undocumented.

In exploring other options, I learned that ImageMagick itself uses another sortware suite, Ghostscript, for PDF rendering. Ghostscript does not have Python bindings, so we make a call to it via a subprocess and pipe the output into a buffer variable. 

(This whole process was so traumatic that [Catherine blogged about it](http://catmores.co/cv/pdf/2014/11/13/teaching-my-computer-to-read-pdfs-are-evil.html). [Twice](http://catmores.co/pdf/2014/11/19/teaching-my-computer-to-read-not-good-enough.html).)




### Michael Zhao
Set up the server.

### Jonathan Jin
Taking on QA and test coverage responsibilities for the front-end tests. Designed the preliminary front-end testing framework that, as of 11/19/14, comprises the primary front-end test suite.

## Evolution
One of the major ways in which our current implementation differs from our initial design is the architecture and design portion of the backend. We designed a somewhat elaborate class diagram to structure our document data. Once we started writing code, however, we realized that the PDF data would best be handled by a pipe-and-filter architecture, and so our approach became more functional, implementing no Python classes at all.

