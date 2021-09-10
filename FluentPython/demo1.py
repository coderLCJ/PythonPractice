# -*- coding: utf-8 -*-
import math

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # 字符串表示形式
    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    # hypot求模
    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return Vector(self.x*other, self.y*other)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


v2 = Vector(1, 2)
v3 = Vector(2, 3)
v1 = Vector(1, 2)
print(v1 == v2)
print(v1 == v3)

x = [i for i in range(10)]
print(x)
