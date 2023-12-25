#6. Режимы доступа public, private, protected. Сеттеры и геттеры
from accessify import private, protected

class Point:
    def __init__(self, x=0, y=0) -> None:
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("value type error")

    @private
    @classmethod
    def __check_value(cls, val):
        # return type(val) in (int, float)
        return isinstance(val, (int, float))

    def set_coord(self, x, y):
        # if type(x) in (int, float) and type(y) in (int, float):
        # if isinstance(x, (int, float)) and isinstance(y, (int, float)):
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("value type error")

    def get_coord(self):
        return (self.__x, self.__y)


pt = Point(11, 11)
pt.set_coord(1234, 5432)

print(pt.get_coord())
print(dir(pt))
