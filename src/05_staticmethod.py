#5. Методы класса (classmethod) и статические методы (staticmethod)

class Vector:
    MAX_COORD = 100
    MIN_COORD = 0

    @staticmethod
    def norm2(x, y):
        return x**2 + y**2
        # return x**2 + y**2 + Vector.MAX_COORD

    def __init__(self, x, y):
        self.x = x
        self.y = y
        print("__init__:", self.norm2(x, y))

    def get_coord(self):
        return self.x, self.y


v = Vector(11, 11)
print(v.get_coord())
# __init__: 242
# (11, 11)


print(v.norm2(3, 4))
# 25
