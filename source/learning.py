#!/usr/bin/env python2

import cv2, os, sys 
from get_mask.accuracy_estimation import estimate_accuracy
from get_mask.searching_methods import searching_methods_table

class Learning_materials:
    def __init__(self, test_file, standard_file):
        self.test = test_file
        self.standard = standard_file

def collect_learning_materials():
    standards_path = "./learning/standards/"
    tests_path = "./learning/tests/"
    materials = []
    for standard in os.listdir(standards_path):
        name = os.path.splitext(standard)[0]
        test = next((f for f in os.listdir(tests_path) \
                     if name == os.path.splitext(f)[0]),
                    None)
        if test: 
            materials.append(Learning_materials(tests_path + test,
                                                standards_path + standard))

    return materials

def run_learning ():
    materials = collect_learning_materials()
    for line in sys.stdin:
        line = line.rstrip('\n')
        d = line.split()
        mclass = searching_methods_table[d[0]]
        method = mclass.parse_args(d[1:])
        score = 0
        for m in materials:
            standard_img = cv2.imread(m.standard, 0)
            test_img = cv2.imread(m.test, 0)
            score += estimate_accuracy(method, test_img, standard_img)
        
        if score > 1: print ' '.join([str(score), line])

if __name__ == "__main__":
    run_learning()
