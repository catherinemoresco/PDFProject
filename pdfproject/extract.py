import subprocess
import cv2
import io
import numpy as np

def getStream(filename):
    ## run ghostscript command as a subprocess and get output
    print filename
    pipe = subprocess.Popen("gs -dNOPAUSE -sDEVICE=jpeg -sOutputFile=%stdout -dJPEGQ=100 -r300 -q "+ filename + " -c quit", stdout=subprocess.PIPE, shell=True)
    out, err = pipe.communicate()


    bytes = io.BytesIO(out)
    stream = bytes.read()

    return stream



def extractImages(filename): 
    stream = getStream(filename)

    print "extracting..."
    imgstart = 0
    imgend = 0
    i = 0

    ## parse for jpgs
    decoded_images = []
    while True:
        next_img_start = stream.find(b'\xff\xd8', i)
        if next_img_start < 0:
            break
        next_img_end = stream.find(b'\xff\xd9', i)
        if next_img_end < 0:
            break
        decoded_image = cv2.imdecode(np.fromstring(stream[next_img_start:next_img_end+2], np.uint8), cv2.CV_LOAD_IMAGE_COLOR)
        decoded_images.append(decoded_image)
        i = next_img_end + 2
    print "images found: " + str(len(decoded_images))
    return decoded_images

