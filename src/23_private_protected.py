#23. Наследование. Атрибуты private и protected

class Geom:
    name = "Geom"

    def __init__(self, x1, y1, x2, y2):
        print(f"Geom.__init__ for {self.__class__}")
        self._verify_coord(x1)
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

    def _verify_coord(self, coord):
        return 0 <= coord <= 255


class Rect(Geom):
    name = "Rect"

    def __init__(self, x1, y1, x2, y2, fill=None):
        super().__init__(x1, y1, x2, y2)
        self._verify_coord(x1)
        self._fill = fill

    def get_coords(self):
        return (self._x1, self._y1)


r = Rect(0, 0, 10, 20)
# Geom.__init__ for <class '__main__.Rect'>

print(r.__dict__)
# {'_x1': 0, '_y1': 0, '_x2': 10, '_y2': 20, '_fill': None}

print(r.get_coords())
# (0, 0)
