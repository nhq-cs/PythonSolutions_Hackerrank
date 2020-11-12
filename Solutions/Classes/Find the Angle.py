import math

class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __sub__(self, other):
        xVector = self.x - other.x
        yVector = self.y - other.y
        zVector = self.z - other.z
        return (Points(xVector, yVector, zVector))
    def dot(self, other):
        ans = self.x*other.x + self.y*other.y + self.z*other.z
        return ans
    def cross(self, other):
        xCross = self.y*other.z - self.z*other.y
        yCross = self.z*other.x - self.x*other.z
        zCross = self.x*other.y - self.y*other.x
        return Points(xCross, yCross, zCross)
    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

if __name__ == '__main__':
