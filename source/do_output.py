
import cv2 as cv
from pathname_utils import filename_with_altext

def stat_format(stat, of, scale=None):
    s = stat
    stream = open(of, 'w')
    if scale is None:
        fp = '{}: {}\n'
    else:
        fp = '{}: {} {}^2\n' # every value means area
    for g in ['mean', 'median', 'std', 'S']:
        x = s[g]
        if scale is not None:
            x = x * pow(scale.factor, 2)
        stream.write(fp.format(g, x, scale.unit))

def contour_parameters (c, scale_factor=None):
    import math
    x, y, w, h = cv.boundingRect(c)
    s = cv.contourArea(c)
    p = cv.arcLength(c, True)

    if scale_factor is not None:
        w, h, p = map(lambda x: float(x)*scale_factor,
                      (w, h, p))
        s = float(s)*pow(scale_factor,2)
    
    d_l = float(p)/math.pi
    d_s = 2*math.sqrt(float(s)/math.pi)
    d = math.sqrt(w*w+h*h)

    return w, h, s, p, d_l, d_s, d

dataRowFormatter = '{:>5d} {:>9.2f} {:>9.2f} {:>9.1f}' + \
                   ' {:>9.2f} {:>9.2f} {:>9.2f} {:>9.2f}  {}\n'
def contour_parameters_row(c, t, i, scale_factor=None):
    plist = list(contour_parameters(c, scale_factor))
    plist.insert(0, i)
    plist.append(t)
    string = dataRowFormatter.format(*plist)
    return string

unit_line_formatter = '# length unit: 1 {}, per pixel: {:.2} {}\n'
column_names = "#   i      w         h          s        p      " + \
               "   d_l       d_s        d     type\n"
def do_output(data, output_file, scale=None):
    img = data.origimg
    
    stat_format(data.stat,
                filename_with_altext(output_file, "txt"),
                scale=scale)
    tabf = open(filename_with_altext(output_file, "dat"), 'w')

    if scale is None:
        scale_factor=None
    else:
        scale_factor=scale.factor
        tabf.write(unit_line_formatter.format(scale.unit,
                                              scale.factor,
                                              scale.unit))
    tabf.write(column_names)

    i = 0 
    for cnt in data.contours:
        cv.drawContours(img, data.contours, i, (90, 204, 0), -1)
        i+=1
        tabf.write(contour_parameters_row(cnt, 'single', i, 
                                          scale_factor=scale_factor))

    j=0
    for cnt in data.ags: 
        cv.drawContours(img, data.ags, j, (32, 203, 240), -1)
        j+=1
        i+=1
        tabf.write(contour_parameters_row(cnt, 'ag', i, 
                                          scale_factor=scale_factor))

    tabf.close()                    
    cv.imwrite(output_file, img)
