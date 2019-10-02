
import cv2 as cv
import numpy as np

def contours_stat(contours):
    s = {}
    areas = map(cv.contourArea, contours)
    s['mean'] = np.mean(areas)
    # s['average'] = np.average(areas)
    s['median'] = np.median(areas)
    s['std'] = np.std(areas)
    s['S'] = sum(areas)
    return s
