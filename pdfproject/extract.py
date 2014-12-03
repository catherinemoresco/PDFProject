import subprocess
import cv2
import io
import numpy as np

def getStream(filename):
    """ converts PDF to series of JPGs, and returns bytestream of output """
    print filename

    ## A call to Ghostscript that rasterizes the PDFs and outputs JPGs.
    ## The output is redirected to stdout, which is piped back into the variable `out`.
    pipe = subprocess.Popen("gs -dNOPAUSE -sDEVICE=jpeg -sOutputFile=%stdout -dJPEGQ=100 -r300 -q "+ filename + " -c quit", stdout=subprocess.PIPE, shell=True)
    out, err = pipe.communicate()

    ## Convert output to bytestream and return
    bytes = io.BytesIO(out)
    stream = bytes.read()

    return stream



def extractImages(filename): 
    """ Parses bytestream of JPGs, and returns a list of the images represented as numpy arrays """
    stream = getStream(filename)

    ## Parse stream byte by btye.
    ## Every JPG begins with b'\xff\xd8' and ends with b'\xff\xd9'.
    ## These delimiters are used to separate the images.
    imgstart = 0
    imgend = 0
    i = 0

    decoded_images = []
    while True:
        next_img_start = stream.find(b'\xff\xd8', i)
        if next_img_start < 0:
            break
        next_img_end = stream.find(b'\xff\xd9', i)
        if next_img_end < 0:
            break
    ## Images are decoded with OpenCV, which represents them as NumPy arrays.
        decoded_image = cv2.imdecode(np.fromstring(stream[next_img_start:next_img_end+2], np.uint8), cv2.CV_LOAD_IMAGE_COLOR)
        decoded_images.append(decoded_image)
        i = next_img_end + 2
    ## Return decoded images
    return decoded_images


def getThumbnailImage(path, filename):
    """ Get image thumbnail and write to file as a png, returning no value """
    path_to_image = path+"/"+filename
    thumbnail_name = path_to_image + "thumb.jpeg"
    pipe = subprocess.Popen("gs -dNOPAUSE -sDEVICE=jpeg -sOutputFile="+thumbnail_name+ " -dLastPage=1 -dJPEGQ=100 -r100 -q "+ path_to_image + " -c quit", shell=True)
    ## ensures file is written before function ends
    pipe.communicate()