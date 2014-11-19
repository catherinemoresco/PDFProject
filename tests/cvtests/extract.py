import PythonMagick
import PyPDF2
import numpy as np 
import base64
import cv2

## test image for development
pdf_im = file('testimg/testpdf.pdf', "rb")

def extractImages(pdf):
    images = []

    pdf_im = PyPDF2.PdfFileReader(pdf)
    npage = pdf_im.getNumPages()

    for p in range(0, npage):
        img = PythonMagick.Image()
        blob = PythonMagick.Blob()
        img.density("75")
        ## read in pdf
        img.read("testimg/testpdf.pdf[" + str(p) + "]") 

        ## write to buffer
        img.write(blob, 'RGB', 16)
        rawdata =  base64.b64decode(blob.base64())

        ## convert raw data to np array
        img = np.ndarray((img.rows(), img.columns(), 3),dtype='uint16', buffer=rawdata)
        images.append(img)
    return images


# cv2.namedWindow("w")
# images = extractImages(pdf_im)
# cv2.imshow("w", images[0])
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# cv2.imwrite("hello.jpg", images[0]/255)

