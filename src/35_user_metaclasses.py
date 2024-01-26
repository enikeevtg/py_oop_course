#35. Пользовательские метаклассы. Параметр metaclass

# функция-метакласс
def create_class_point(name, base, attrs):
    attrs.update({"MAX_COORD": 100, "MIN_COORD": 0})
    return type(name, base, attrs)


class Point(metaclass=create_class_point):
    def get_coord(self):
        return (0, 0)


pt = Point()
print(pt.MAX_COORD)
print(pt.get_coord())
# 100
# (0, 0)


# класс-метакласс
class Meta(type):
    def __new__(cls, name, base, attrs):
        attrs.update({"MAX_COORD": 101, "MIN_COORD": 1})
        return type.__new__(cls, name, base, attrs)

    # def __init__(cls, name, base, attrs):
    #     super().__init__(name, base, attrs)
    #     cls.MAX_COORD = 101
    #     cls.MIN_COORD = 1


class Point(metaclass=Meta):
    def get_coord(self):
        return (1, 1)

pt = Point()
print(pt.MAX_COORD)
print(pt.get_coord())
# 101
# (1, 1)
