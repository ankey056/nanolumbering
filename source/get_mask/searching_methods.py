
from image_parameters import Image_parameters
import numpy as np
import cv2

from searching_methods_text_protocol \
 import Intensity_filtering_inside_out as IFioM
from searching_methods_text_protocol import Intensity_filtering as IFM

def intensity_filtrate (img, minimal_intensity = None,
                        maximal_intensity = None):

    f = np.ones(img.shape, np.bool)
    if minimal_intensity: f[img<minimal_intensity] = False
    if maximal_intensity: f[img>maximal_intensity] = False

    return f

class Intensity_filtering(IFM):
    def apply (self, img):
        r = self.r
        b = cv2.GaussianBlur(img, (r, r), self.sigma)

        imp = Image_parameters(img)
        x = imp.get_real_range(self.rimin, self.rimax)
        minimal_intensity, maximal_intensity = x

        return intensity_filtrate(b, minimal_intensity, maximal_intensity)

class Intensity_filtering_inside_out(IFioM):
    def apply (self, img):
        imp = Image_parameters(img)
        x = imp.get_real_range(self.rimin, self.rimax)
        minimal_intensity, maximal_intensity = x

        res = 255 * np.ones(img.shape, np.int8)
        res[img<minimal_intensity] = 0
        res[img>maximal_intensity] = 0

        r = self.r
        b = cv2.GaussianBlur(img.copy(), (r, r), self.sigma)

        return intensity_filtrate(res, 5)

searching_methods = ( Intensity_filtering,
                      Intensity_filtering_inside_out)

searching_methods_table = {}

for method in searching_methods:
    searching_methods_table[method.name] = method
