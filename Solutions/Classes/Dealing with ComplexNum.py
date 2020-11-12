import math

class Complex(object):
    def __init__ (self, re, im):
        self.re = re
        self.im = im
    def __add__ (self, other):
        reAdd = self.re + other.re
        imAdd = self.im + other.im
        return Complex(reAdd, imAdd)
    def __sub__ (self, other):
        reSub = self.re - other.re
        imSub = self.im - other.im
        return Complex(reSub, imSub)
    def __mul__(self, other):
        reMul = self.re*other.re - self.im*other.im
        imMul = self.re*other.im + self.im*other.re
        return Complex(reMul, imMul)
    def __truediv__(self, other):
        denom = pow(other.re,2) + pow(other.im,2)
        reDiv = (self.re*other.re + self.im*other.im)/denom
        imDiv = (-self.re*other.im +self.im*other.re)/denom
        return Complex(reDiv, imDiv)
    def mod(self):
        reMod = pow((self.re**2+self.im**2),0.5)
        imMod = 0.00
        return Complex(reMod, imMod)
    def __str__(self):
        if self.im == 0:
            result = "%.2f+0.00i" % (self.re)
        elif self.re== 0:
            if self.im >= 0:
                result = "0.00+%.2fi" % (self.im)
            else:
                result = "0.00-%.2fi" % (abs(self.im))
        elif self.im > 0:
            result = "%.2f+%.2fi" % (self.re, self.im)
        else:
            result = "%.2f-%.2fi" % (self.re, abs(self.im))
        return result

if __name__ == '__main__':