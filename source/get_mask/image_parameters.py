
class Image_parameters:

    def __init__(self, img):
        meani = img.sum()/img.size
        maxi = img.max()
        self.maxi = maxi
        self.meani = meani
        self._delta = maxi - meani

    def relative2abs (self, x):
        return self.meani + self._delta*x

    def get_real_range (self, rmin, rmax):
        return self.relative2abs(rmin), self.relative2abs(rmax)
