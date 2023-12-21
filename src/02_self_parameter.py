#2. Методы классов. Параметр self

# class Point
class Point:
    """some documentation"""

    color = "red"
    size = 3

    def set_coords():
        print("вызов метода set_coords")

    def set_coords_2(self):
        print("вызов метода set_coords_2", str(self))

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_coordinates(self):
        return (self.x, self.y)


# вызов метода без параметра self напрямую из класса
print(Point.set_coords)
Point.set_coords()
# <function Point.set_coord at 0x7fd932ee79a0>
# вызов метода set_coords


# вызов метода с параметром self через объект класса
pt = Point()
print(pt)
pt.set_coords_2()
# <__main__.Point object at 0x7ff152f90070>
# вызов метода set_coords_2 <__main__.Point object at 0x7ff152f90070>


# вызов метода с параметром self напрямую из класса
Point.set_coords_2(pt)
# вызов метода set_coords_2 <__main__.Point object at 0x7f5efb390070>


# вызов метода, создающего локальные аттрибуты объекта
pt.set_coordinates(11, 11)
print(pt.__dict__)
# {'x': 11, 'y': 11}


# вызов геттера напрямую и через getattr()
print(pt.get_coordinates())
f = getattr(pt, "get_coordinates")
print(f())
# (11, 11)
# (11, 11)
