
import cv2 as cv
import numpy as np

minI = 0.035

def Ifun (contour, P):
    return cv.contourArea(contour)/pow(P,2)


def dumtest(contour, darlim):
    P = cv.arcLength(contour, True)
    if P < 5: return False

    x, y, w, h = cv.boundingRect(contour)
    if (w < 6) or (h < 6): return False

    I = Ifun(contour, P)

    return  cv.contourArea(contour) >= darlim

def cntd(c):
    x, y, w, h = cv.boundingRect(c)
    return w*w+h*h

def slim(cnts):
    v = map(cntd, cnts)
    return np.average(v) + 1.2 * np.std(v)

def test_contour(contour, sizelim):
    P = cv.arcLength(contour, True)
    I = Ifun(contour, P)

    return  (I >= minI) and (cntd(contour) < sizelim)


def sel_contours (contours, stat):
    c = list()

    darlim = stat['mean']/5

    for ci in contours:
        if dumtest(ci, darlim): c.append(ci)

    cnts = list()
    ags = list()
    sizelim = slim(c)

    for ci in c:
        if test_contour(ci, sizelim):
            cnts.append(ci)
        else:
            ags.append(ci)

    return cnts, ags
