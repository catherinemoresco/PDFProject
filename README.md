# The PDF Project 

*For Software Construction Fall 2014*

## Team Members

- [ Catherine Moresco ](https://github.com/catherinemoresco/)
- [ Jonathan Jin ](https://github.com/jinnovation)
- [ Megan Barnes ](https://github.com/meganbarnes)
- [ Michael Zhao ](https://github.com/ucmz)
- Alberto Rios
- [ Cristian Saucedo ](https://github.com/saucedoc)

## Setup

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
Install python packages with `pip install -r <path/to/requirements.txt>`.

Third party packages (see respective websites for installation instructions):

- [OpenCV2](http://opencv.org/)
- [Ghostscript](http://ghostscript.com/doc/current/Install.htm)

## How to Run
After installing dependencies, you can run the app locally with 
`python runserver.py`.

For automatic server-crash recovery, install [ supervisord
](http://supervisord.org/) and start the server using `run.sh`.

## Example Usage
It's pretty simple to use: upload your own document with the "upload" button,
  and watch it appear, processed and straightened!

The best images are ones that are well formed, and have only one page of text
per PDF page. Images embedded in the text are OK!

There is a sample PDF document: `tests/tryme.pdf`.

## Note

See the wiki for more info.
