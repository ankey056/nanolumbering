
import cv2, sys
import numpy as np
from searching_methods import searching_methods_table

intensity_range = [0.4, 1.0]

def load_methods ():
    methods = []
    with open("./learning/model/table.txt", "r+") as f:
        for line in f:
            line = line.rstrip('\n')
            d = line.split()
            factor = float(d[0])
            mclass = searching_methods_table[d[1]]
            method = mclass.parse_args(d[2:])
            method.factor = factor

            methods.append(method)

    return methods

methods = 0

def init_system():
    global methods
    methods = load_methods()

def eval_total_image (source):
    s = 0
    for m in methods: s += m.factor * m.apply(source)
    return s

def finalize_result (total_image):
    zero = 0
    mask = 255
    
    imax = np.max(total_image)
    rimin, rimax = intensity_range
    r = mask * np.ones(total_image.shape, np.int8) 
    r[total_image < rimin*imax] = zero
    if rimax < 1.0: r[total_image > rimax*imax] = zero

    return r

def get_mask (img):
    return finalize_result(eval_total_image(img))

if __name__ == "__main__":
    methods = load_methods()
    gr = cv2.imread(sys.argv[1],0)
    cv2.imwrite(sys.argv[2], finalize_result(eval_total_image(gr)))
