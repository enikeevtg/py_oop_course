#20. Наследование в объектно-ориентированном программировании

class Geom:
    name = "Geom"

    def set_coords(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def draw(self):
        print("geometry drawing")


class Line(Geom):
    name = "Line"

    def draw(self):
        print("line drawing")


class Rect(Geom):
    def draw(self):
        print("rect drawing")


geom = Geom()
line = Line()
print(line.name)
# Geom

rect = Rect()
rect.draw()
# rect drawing

line.set_coords(1, 1, 5, 3)
rect.set_coords(0, 0, 1, 2)
print(line.__dict__)
print(rect.__dict__)
# {'x1': 1, 'y1': 1, 'x2': 5, 'y2': 3}
# {'x1': 0, 'y1': 0, 'x2': 1, 'y2': 2}
