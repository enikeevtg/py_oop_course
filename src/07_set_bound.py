#7. Магические методы __setattr__, __getattribute__, __getattr__ и __delattr__

from typing import Any


class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    @classmethod
    def __check_coord(cls, x, y):
        return (cls.MIN_COORD <= x <= cls.MAX_COORD and
                cls.MIN_COORD <= y <= cls.MAX_COORD)

    def __init__(self, x=0, y=0):
        self.x = 0
        self.y = 0
        if self.__check_coord(x, y):
            self.x = x
            self.y = y

    def get_coord(self):
        return self.x, self.y

    def set_bound_wrong(self, val):
        self.MIN_COORD = val

    @classmethod
    def set_bound(cls, val):
        cls.MIN_COORD = val

    def __getattribute__(self, __name: str) -> Any:
        print("__getattribute__")
        return object.__getattribute__(self, __name)


pt = Point(-1, 1000)
print(pt.get_coord())
# (0, 0)


print(pt.__dict__)
pt.set_bound_wrong(-100)
print(pt.__dict__)
print(Point.__dict__)
# {'x': 0, 'y': 0}
# {'x': 0, 'y': 0, 'MIN_COORD': -100}
# {'__module__': '__main__', 'MAX_COORD': 100, 'MIN_COORD': 0, ...}


pt.__delattr__("MIN_COORD")
print(pt.__dict__)
pt.set_bound(-100)
print(pt.__dict__)
print(Point.__dict__)
# {'x': 0, 'y': 0}
# {'x': 0, 'y': 0}
# {'__module__': '__main__', 'MAX_COORD': 100, 'MIN_COORD': -100, ...}
