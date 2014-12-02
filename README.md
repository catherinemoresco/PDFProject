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

