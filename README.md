# The PDF Project 

*For [ University of Chicago CMSC 22001: Software Construction Fall 2014 ](http://people.cs.uchicago.edu/~shanlu/teaching/22001_fa14/index.html)*

## Team Members

- [ Catherine Moresco ](https://github.com/catherinemoresco/)
- [ Jonathan Jin ](https://github.com/jinnovation)
- [ Megan Barnes ](https://github.com/meganbarnes)
- [ Michael Zhao ](https://github.com/ucmz)
- Alberto Rios
- [ Cristian Saucedo ](https://github.com/saucedoc)


## What It Does

Scannd is a web-based PDF viewer+.  You can upload a PDF in your web browser, view it, add
highlights, and export your highlighted PDF file.  Behind the scenes, Scannd is analyzing
your PDF to find text lines for highlighting.  It is also detecting and correcting skew in
your PDF so that it can display nice, easy-to-read horizontal text lines.  Scannd was born
out of a desire for an automated way to clean up often crooked, hard-to-read textbook scans, 
and view them easily in the browser.

## Usage Guide
It's pretty simple to use: once you navigate to [Scannd](http://spark.uchicago.edu), 
upload your own document with the "upload" button, and click the "read" button.

You'll be prompted to manually rotate your PDF until it is right-side up (in case you upload
a PDF that is upside down).  Then watch it appear, processed and straightened!

To add a highlight to a text line, simply highlight the text line with your mouse.  
Double-click to make it disappear.  

Clicking the "export" button will initiate a download of the edited PDF to your desktop.

No installation is necessary, unless you'd like to run our server on your machine (which 
we don't expect).  For that, see 'Advanced Usage' below.

The best images are ones that are well formed, and have only one page of text
per PDF page. Images embedded in the text are OK!

There is a sample PDF document: `tests/tryme.pdf`.

## Avoid...
...inputs that have very curved text lines (mostly a problem with scans of thick textbooks
as far as text near the textbook spine).  Also, we do not expect inputs with a lot of
background noise; solid backgrounds are best.  PDFs with differently oriented pages are not
expected either (one page is rotated 90 degrees, another is rotated 0 degrees).  
Please do not upload PDFs longer than 50 pages.

## Disclaimer
This website is not meant to be responsive.  That means it is not meant for use on mobile
browsers or tiny browser windows.

## Advanced Usage

### Checkout

The project has one submodule -- [jsPDF](https://github.com/MrRio/jsPDF).

To properly clone this repository -- that is, such that the clone contains the
contents of the [jsPDF](https://github.com/MrRio/jsPDF) repository at the
requested commit -- please use the following command:

```
git clone --recursive <repo-path>
```

This is opposed to simply using `git clone`, which would simply create an empty
directory for `jsPDF`, leaving it up to you to initialize all submodules
separately from the main clone.

### Dependencies
#### Submodules
- [jsPDF](https://github.com/MrRio/jsPDF)

In the case that you didn't perform a recursive clone, run the following: 
  
```
git submodule init
```

#### Python Packages
```
pip install -r <path/to/requirements.txt>
```

#### Other

- [OpenCV2](http://opencv.org/)
- [Ghostscript](http://ghostscript.com/doc/current/Install.htm)

See respective websites for download and installation instructions.

### How to Run
After installing dependencies, you can run the app locally with 
`python runserver.py`.

For automatic server-crash recovery, install [ supervisord
](http://supervisord.org/) and start the server using `run.sh`.


## Notable Wiki Articles
- [ Evolution ](https://github.com/catherinemoresco/PDFProject/wiki/Evolution)
- [ Who Did What ](https://github.com/catherinemoresco/PDFProject/wiki/Who-Did-What)
- [ PDF Rasterizing ](https://github.com/catherinemoresco/PDFProject/wiki/PDF-Rasterizing)
- [ Program Structure ](https://github.com/catherinemoresco/PDFProject/wiki/Program-Structure)
- [ Skew Detection ](https://github.com/catherinemoresco/PDFProject/wiki/Skew-Detection)
- [ Postmortem ](https://github.com/catherinemoresco/PDFProject/wiki/Postmortem)
