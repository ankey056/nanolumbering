
from get_mask.get_mask import get_mask
from get_mask.get_mask import init_system as gm_init
import cv2 as cv
from contours_selection import sel_contours, Ifun
from units_parsing import tiff2scale
from objects_stat import contours_stat
from do_output import do_output

class Bunch:
    def __init__(self, **kwds):
        self.__dict__.update(kwds)

def init_system():
    gm_init()

def find_objects(img, scale=None):
    r = Bunch()
    r.origimg = img

    h, w, depth = img.shape
    img = img[0:h-49,:,:]

    r.img = img

    gr = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    m = get_mask(gr).astype('uint8')
    cnts, h = cv.findContours(m,
                              cv.RETR_TREE,
                              cv.CHAIN_APPROX_SIMPLE)

    c, ags = sel_contours(cnts,
                          contours_stat(cnts))
    r.stat = contours_stat(c)
    
    r.ags = ags
    r.contours = c
    r.for_collecting = None
    return r

def process_file (image_file, output_file):
    scale = tiff2scale(image_file)
    data = find_objects(cv.imread(image_file))
    do_output(data, output_file, scale=scale)
    return data.for_collecting

