#!/usr/bin/python3

from math import hypot

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector(%d,%d)'%(self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)


    def __add__(self, other):
        x = self.x + other.x
        y = self.y + self.y
        return Vector(x,y)


    def __mul__(self, scale):
        return Vector(self.x * scale, self.y * scale)

v = Vector(3,4)
print(v)
print(abs(v))

v1 = Vector(3,4)
v2 = Vector(5,6)
v3 = v1 + v2
print(v3)
print(abs(v3))

v3 = v3 * 10
print(v3)
print(abs(v3))
