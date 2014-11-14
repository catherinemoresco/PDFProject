import extract
import skew
import getlines

def process(pdf):
  images = extract.extractImages(pdf)
  map(skew.straighten, images)
  map(getlines.getLines, images)
  return images
