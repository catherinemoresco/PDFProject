# The PDF Project 

*For Software Construction Fall 2014*

Catherine Moresco, Jonathan Jin, Megan Barnes, Michael Zhao, Alberto Rios, and Cristian Saucedo

## Features

## Example Usage

## System Requirements
For automatic server-crash recovery, install supervisord and start the server using `run.sh`.

## Dependencies
Install python packages with `pip install -r <path/to/requirements.txt>`.

Third party packages:

- [OpenCV2](http://opencv.org/)
- [PythonMagick](http://www.imagemagick.org/download/python/)

## How to Run

## How to Run Unit Tests
Computer Vision Unit Tests (Catherine Moresco and Megan Barnes):
from within tests/cvtests, use the command:
`python -m unittest -v cv_unit_tests`

Alberto & Cristian: The unit tests that we initially submitted will not run given the changes in UI. We are looking into automated processes for testing UI that we will incorporate into iteration 2.
## Who did What
##### Alberto & Cristian: 
We were in charge of User Interface design. We created the HTML displayed, worked on uploading files to server, passing files to CV modules, and displaying the resulting files.


##### Catherine & Megan: 
We were in charge of the Computer Vision aspect of the project.  We worked on processing image files in order to determine whether or not they should be rotated and to determine where lines were in text documents.

Michael Zhao set up the server.

## Evolution
While our first iteration of the software construction process did not meet all the grand visions we have for it, it was a good first step. We implemented the basic functions of file uploading, and impage processing and displaying, and laid the groundwork for user interaction with the document. 

One of the major ways in which our current implementation differs from our initial design is the architecture and design portion of the backend. We designed a somewhat elaborate class diagram to structure our document data. Once we started writing code, however, we realized that the PDF data would best be handled by a pipe-and-filter architecture, and so our approach became more functional, implementing no classes at all.

The frontend will likely implement more objects as development continues, although it is unlikely to develop into the complextiy of our original plan. And this isn't necessarily a bad thing! After all, Simplicity is one of the twelve principles behind the Agile Manifesto.

## Additional Information