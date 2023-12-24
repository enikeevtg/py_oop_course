#5. Методы класса (classmethod) и статические методы (staticmethod)

class Vector:
    MAX_COORD = 100
    MIN_COORD = 0

    @classmethod
    def validate(cls, arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD

    def __init__(self, x, y):
        self.x = self.y = 0
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y

    def get_coord(self):
        return self.x, self.y

    @classmethod
    def change_coord(cls, self, x, y):
        self.x = x
        self.y = y


print(Vector.validate(11))
# True


v1 = Vector(11, 11)
v2 = Vector(0, 1000)
print(v1.get_coord())
print(v2.get_coord())
# (11, 11)
# (0, 0)


Vector.change_coord(v2, 8, 351)
print("v2 after Vector.change_coord(v2, 8, 351):", v2.get_coord())
v2.change_coord(v2, 123, 4453)
print("v2 after v2.change_coord(v2, 123, 4453):", v2.get_coord())
# v2 after Vector.change_coord(v2, 8, 351): (8, 351)
# v2 after v2.change_coord(v2, 123, 4453): (123, 4453)
