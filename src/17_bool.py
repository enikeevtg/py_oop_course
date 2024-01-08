#17. Магический метод __bool__ определения правдивости объектов
import math


class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __len__(self):
        print("__len__")
        return int(math.sqrt(self.x ** 2 + self.y ** 2))
    
    def __bool__(self):
        print("__bool__")
        return self.x == self.y

p1 = Point(1, 2)
print(len(p1))
print(bool(p1))
# __len__
# 2
# __bool__
# False

p2 = Point(11, 11)
if p2:
    print("true condition")
else:
    print("false condition")
# __bool__
# true condition
