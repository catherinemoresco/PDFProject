# The PDF Project 

*For Software Construction Fall 2014*

- [ Catherine Moresco ](https://github.com/catherinemoresco/)
- [ Jonathan Jin ](https://github.com/jinnovation)
- [ Megan Barnes ](https://github.com/meganbarnes)
- [ Michael Zhao ](https://github.com/ucmz)
- Alberto Rios
- [ Cristian Saucedo ](https://github.com/saucedox)

## Setup
### Dependencies
Install python packages with `pip install -r <path/to/requirements.txt>`.

Third party packages (see respective websites for installation instructions):

- [OpenCV2](http://opencv.org/)
- [Ghostscript](http://ghostscript.com/doc/current/Install.htm)

### How to Run
After installing dependencies, you can run the app locally with 
`python runserver.py`.

For automatic server-crash recovery, install [ supervisord
](http://supervisord.org/) and start the server using `run.sh`.

## Example Usage and Recommended Acceptance Tests
It's pretty simple to use: upload your own document with the "upload" button,
  and watch it appear, processed and straightened!

The best images are ones that are well formed, and have only one page of text
per PDF page. Images embedded in the text are OK!

There is a sample PDF document: `tests/tryme.pdf`.

## Testing
### How to Run Unit Tests
#### Image Processing Tests:
From within tests/cvtests, run the command `python -m unittest -v
cv_unit_tests`.

The folder `cvtests` contains the test file and copies of source files for our
image processing algorithms.  More specific information about which functions
and what functionality the tests are concerned with is within
`cv_unit_tests.py`.

*- Megan and Catherine*

#### UI Tests:

1. Run the app locally with `python runserver.py`
2. Run the individual test suites with `python tests/uitests/<suite_name>`

 *- Alberto, Cristian, Jonathan*

## Program Structure (Step-by-step)
1. Our web app contains the initial functionality for uploading a PDF.  The
   app's code can be found in `pdfproject/_init_.py`, with functions to handle
   the home screen, as well as uploading.  The front-end is contained within
   `pdfproject/{templates,static}`.

2. Once the user has chosen a PDF to upload, the `upload_file()` function in
   `_init_.py` saves the file to the uploads folder on the server

3. `upload_file()` then calls `processing.process()` from
   `pdfproject/processing.py` on the PDF file to initialize image processing

    1. `process()` first calls `extract.extractImages()` from
       `pdfproject/extract.py` in order to pull images (.jpg) representing
       each page of the PDF from the file.  These will be passed to the rest
       of the image processing functions.

    2. `process()` calls `skew.straighten()` (from `pdfproject/skew.py`) on
       each of the images, which first uses `skew.horizontal_sums()` to help
       calculate the probable skew angle of the input image and then
       `skew.rotate()` to generate an image rotated at that angle.  It
       returns a rotated image for every input image.

    3. `process()` calls `getlines.getLines()` on each straightened image.
       `getLines()` calls its helper function, `getlines.isolateLines()`
       which contains the entire algorithm for creating a grayscale image
       which has black where blank space should be and white where it thinks
       there are text lines.  `getLines()` then detects the pixel
       coordinates of the lines and returns them in a list.

4. `processing.process()` gathers the lines and puts them in a dictionary,
   mapped to their page number as a key.  The dictionary is returned as a json
   string.

5. Passing the json string back to the web app as a ....json.txt file,
   `upload_file()` in `_init_.py` redirects to a page which corresponds to the
   uploaded_file() function in `_init_.py`, which displays each of the processed
   images that were returned after straightening and reads the line coordinates
   for highlighting from the ....json.txt file.  The page is once again rendered
   using html/css/javascript from `pdfproject/templates` and
   `pdfproject/static`.

6. Annotations are rendered as SVG objects on the page.

7. The user will be able to export their annotations. We use Javascript
   libraries, in particular [ jsPDF ](https://parall.ax/products/jspdf), to keep
   this processing on the client side.

### Data Flow Diagram
A data flow diagram for our backend processes is provided below.

![](readme-assets/dataflowdiagram.jpg)

Our architecture resembles a hybrid between a pipe-and-filter and data-centered
architecture. A pipe-and-filter architecture makes sense for our task, because
image processing consists mostly of passing the PDF and image data through a
series of filter that modifies said data and extracts needed information.

Our decision to implement the project as a web application makes writing to and
reading from memory a necessity; it is the method most suited to passing file
data from one app route to the next.

## Evolution
One of the major ways in which our current implementation differs from our
initial design is the architecture and design portion of the backend. We
designed a somewhat elaborate class diagram to structure our document data. Once
we started writing code, however, we realized that the PDF data would best be
handled by a pipe-and-filter architecture, and so our approach became more
functional, implementing no Python classes at all.

As a reminder, our original class diagram looked like this:

![](readme-assets/ClassDiagrams.jpg)

Instead of implementing this structure, we use no classes, and instead (in the
backend) only use a list of filenames referring to images of pages and their
corresponding line data to refer to a document. The edits and annotations are
never managed in the backend at all, but constructed and rendered directly in
the DOM.

(See the data flow diagram in "Program Structure" for details on our updated
 design.)

