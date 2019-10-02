
class Searching_method:
    name = "" 

    def __init__(self, p):
        self.parameters = p or []

    def __str__(self):
        s = ' '
        return self.name + s + s.join(self.parameters)

class Intensity_filtering(Searching_method):
    name = "intensity-filtering"

    def __init__(self, r, sigma, rimin, rimax):
        self.r = r
        self.sigma = sigma
        self.rimin = rimin
        self.rimax = rimax

    def __str__(self):
        self.parameters = [self.rmin, self.rmax]
        return super(Intensity_filtering, self).__str__()

    @classmethod
    def parse_args(cls, args):
        r = int(args[0])
        sigma = float(args[1])
        rimin = float(args[2])
        rimax = float(args[3])
        return cls(r, sigma, rimin, rimax)
        
class Intensity_filtering_inside_out(Intensity_filtering):
    name = "intensity-filtering-inside-out"
