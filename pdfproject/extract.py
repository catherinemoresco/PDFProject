import PythonMagick
import PyPDF2
import numpy as np 
import base64

## test image for development
pdf_im = PyPDF2.PdfFileReader(file('testimg/testpdf.pdf', "rb"))

def extractImages(pdf):
    images = []
    pdf_im = PyPDF2.PdfFileReader(pdf)
    npage = pdf_im.getNumPages()

    for p in range(0, npage):
        img = PythonMagick.Image()
        blob = PythonMagick.Blob()
        img.density("300")
        img.read("testimg/testpdf.pdf[" + str(p) + "]") # read in at 300 dpi
        img.write(blob, 'JPG')

        rawdata =  base64.b64decode(blob.base64())

        ## this step currently not working
        img = np.ndarray((img.rows(), img.columns(), 2),dtype='uint16', buffer=rawdata)
        images.append(img)
    print images

