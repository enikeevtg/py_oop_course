#22. Наследование. Функция super() и делегирование

class Geom:
    name = "Geom"

    def __init__(self, x1, y1, x2, y2):
        print(f"Geom.__init__ for {self.__class__}")
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


class Line(Geom):
    name = "Line"

    # # вынесено в базовый класс
    # def __init__(self, x1, y1, x2, y2):
    #     self.x1 = x1
    #     self.y1 = y1
    #     self.x2 = x2
    #     self.y2 = y2

    def draw(self):
        print("Line.draw")


class Rect(Geom):
    name = "Rect"

    def __init__(self, x1, y1, x2, y2, fill=None):
        super().__init__(x1, y1, x2, y2)
        self.fill = fill

    def draw(self):
        print("Rect.draw")


l = Line(0, 0, 11, 22)
r = Rect(0, 0, 11, 22)
# Geom.__init__ for <class '__main__.Line'>
# Geom.__init__ for <class '__main__.Rect'>

print(l.__dict__)
print(r.__dict__)
# {'x1': 0, 'y1': 0, 'x2': 11, 'y2': 22}
# {'x1': 0, 'y1': 0, 'x2': 11, 'y2': 22, 'fill': None}
