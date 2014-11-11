#------------------------------------------------------------------------------#
#                       Create Markov(?) Chains                                #
#                     ---------------------------                              # 
#    Author:    Michael Sverdlin                                               #
#    Date:      14/6/08                                                        #
#                                                                              #
#    TODO:                                                                     #
#                                                                              #
#    (c) copyright 2008-2009                                                   #
#------------------------------------------------------------------------------#
#----------------------------------IMPORTS-------------------------------------#

import os
import re
import sys
import time

from PIL import Image

#----------------------------------GLOBALS-------------------------------------#

PPM_MAGIC = "P6"

#----------------------------------CLASSES-------------------------------------#

#---------------------------------FUNCTIONS------------------------------------#

#-----------------------------------MAIN---------------------------------------#

def main():
    """
    Entry point... You enter here.
    """
    assert 3 == len(sys.argv), "Wrong usage. Usage: %s <input_ppm_image> <output_jpg_image>." % sys.argv[0]
    
    input_image = sys.argv[1]
    assert os.path.isfile(input_image), "The input image %s doesn't exist." % input_image
    
    output_place = sys.argv[2]
    
    input_text = open(input_image, 'rb').read()
    assert PPM_MAGIC == input_text[:2], "The image inputted (%s) doesn't have the right magic!" % input_image
    
    input_text = input_text[3:]
    image_width, image_height, max_color = re.findall("(\d+)\s+(\d+)\s+(\d+)\s+", input_text)[0]

    to_remove = re.findall("(\d+\s+\d+\s+\d+\s+)", input_text)[0]
    input_text = input_text.replace(to_remove, "")
    
    new_img = Image.new("RGB", (int(image_width), int(image_height)))
    
    for i in xrange(int(image_height)):
        for j in xrange(int(image_width)):
            r, g, b = tuple(input_text[:3])
            #print ord(r), ord(g), ord(b), r, g, b
            input_text = input_text[3:]
            new_img.putpixel((j, i), (ord(r), ord(g), ord(b)))
    
    new_img.save(output_place)
    
            
if "__main__" == __name__:
    try:
        xxx = time.time()
        main()
        print "Running the program took %s seconds." % (time.time() - xxx)
    except:
        print "The program crashed. Here's why:"
        import traceback
        traceback.print_exc()