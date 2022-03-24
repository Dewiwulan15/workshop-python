#In that case, arguments given to the class instantiation operator are passed on to __init__()
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
x = Complex(3.0, -4.5)
x.r, x.i

#ouput
"""
(3.0, -4.5)
"""