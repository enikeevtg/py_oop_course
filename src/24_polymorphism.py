#24. Полиморфизм и абстрактные методы

class Geom:
    def get_pr(self):
        raise NotImplementedError("В дочернем классе должен быть определён\
 метод get_pr()")


class Rectangle(Geom):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_pr(self):
        '''расчёт периметра прямоугольника'''
        return 2 * (self.w + self.h)


class Square(Geom):
    def __init__(self, a):
        self.a = a

    def get_pr(self):
        '''расчёт периметра квадрата'''
        return 4 * self.a


class Triangle(Geom):
    def __init__(self, a, b, c) -> None:
        self.a = a
        self.b = b
        self.c = c

    def get_pr(self):
        return self.a + self.b + self.c


r1 = Rectangle(1, 2)
r2 = Rectangle(3, 4)
s1 = Square(10)
s2 = Square(20)
print(r1.get_pr(), r2.get_pr())
print(s1.get_pr(), s2.get_pr())
# 6 14
# 40 80

objects = [Rectangle(1, 2), Rectangle(3, 4),
           Square(10), Square(20),
           Triangle(1, 2, 3), Triangle(4, 5, 6)]

for obj in objects:
    print(obj.get_pr(), end=" ")
# 6 14 40 80 6 15
