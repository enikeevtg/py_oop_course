#13. Магические методы __str__, __repr__, __len__, __abs__

class Point:
    def __init__(self, *args):
        self.__coords = args

    def __len__(self):
        return len(self.__coords)

    def __abs__(self):
        return list(map(abs, self.__coords))

pt = Point(-1, -2, -3)
print(len(pt))
print(abs(pt))
# 3
# [1, 2, 3]
