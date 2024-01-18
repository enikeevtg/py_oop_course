#27. Как работает __slots__ с property и при наследовании

class Point2D:
    __slots__ = ('x', 'y', '__length')

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.__length = (x * x + y * y) ** 0.5

    @property
    def length(self):
        return self.__length
    
    @length.setter
    def length(self, val):
        self.__length = val


class Point3D(Point2D):
    __slots__ = 'z',

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


pt = Point2D(1, 1)
print(pt.length)
pt.length = 1
print(pt.length)
# 1.4142135623730951
# 1

pt3 = Point3D(1, 2)
print(pt3.y)
pt3.z = 1
pt3.a = 0
# 2
# AttributeError: 'Point3D' object has no attribute 'a'
