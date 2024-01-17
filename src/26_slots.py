#26. Коллекция __slots__

import timeit

class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def time_calc(self):
        self.x += 1
        del self.y
        self.y = 0


class Point2D:
    __slots__ = ('x', 'y')

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def time_calc(self):
        self.x += 1
        del self.y
        self.y = 0


pt1 = Point(1, 1)
pt1.z = 1

pt2 = Point2D(2, 2)
# pt2.z = 2
# ...
# AttributeError: 'Point2D' object has no attribute 'z'

# print(pt2.__dict__)
# ...
# AttributeError: 'Point2D' object has no attribute '__dict__'. Did you mean: '__dir__'?

print(pt1.__sizeof__() + pt1.__dict__.__sizeof__())
print(pt2.__sizeof__())
# 120
# 32

t1 = timeit.timeit(pt1.time_calc)
t2 = timeit.timeit(pt2.time_calc)
print(t1, t2)
# 0.4973447179654613 0.26447843096684664
