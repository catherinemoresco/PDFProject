import PythonMagick
import PyPDF2
import numpy as np 
import base64
import cv2

imgname = "testimg/Biagioli_GalileoCourtier.pdf"

## test image for development
pdf_im = file(imgname, "rb")

def extractImages(pdf):
    images = []

    pdf_im = PyPDF2.PdfFileReader(pdf)
    npage = pdf_im.getNumPages()

    for p in range(0, 5):
        img = PythonMagick.Image()
        blob = PythonMagick.Blob()
        img.density("75")
        img.antiAlias(True)

        ## read in pdf

        img.read(imgname + "[" + str(p) + "]") 


        ## write to buffer
        img.write(blob, 'RGB', 16)
        rawdata =  base64.b64decode(blob.base64())

        ## convert raw data to np array
        img = np.ndarray((img.rows(), img.columns(), 3),dtype='uint16', buffer=rawdata)
        # img = cv2.GaussianBlur(img, (3,3),1)
 
        images.append(img)
    return images


cv2.namedWindow("w")
images = extractImages(pdf_im)
# cv2.imshow("w", images[4])
# cv2.waitKey(0)
# cv2.destroyAllWindows()
cv2.imwrite("hello.jpg", images[4]/255)

