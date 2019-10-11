
from PIL import Image
# import sys

class Scale:
    def __init__ (self, factor, unit):
        self.factor = factor
        self.unit = unit

def tiff2scale (filename):

    img = Image.open(filename, 'r')

    l = img.tag.items()[4][1][0].splitlines()
    ix = l.index(u'AP_PIXEL_SIZE')

    xstring = l[ix+1] # typical value is u'Pixel Size = 2.0 nm'
    xstring2 = xstring[13:] # cut off 'Pixel Size = '

    x, u = xstring2.split()
    x = float(x)

    return Scale(x, u)
