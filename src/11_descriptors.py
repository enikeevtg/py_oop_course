#11. Дескрипторы (data descriptor и non-data descriptor)

# data descriptor
class Coordinate:
    @classmethod
    def __check_coord(cls, coord):
        if not isinstance(coord, (int, float)):
            raise TypeError("Координата должна быть числом")

    def __set_name__(self, owner, name):
        self.name = f"_{name}"

    # def __get__(self, instance, owner):
        # return instance.__dict__[self.name]
    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    # def __set__(self, instance, value):
        # print(f"Coordinate.__set__: {self.name} = {value}")
        # self.__check_coord(value)
        # instance.__dict__[self.name] = value
    def __set__(self, instance, value):
        self.__check_coord(value)
        setattr(instance, self.name, value)


# non-data descriptor
class ReadCoordinate:
    def __set_name__(self, owner, name):
        self.name = f"_{name[0]}"

    def __get__(self, instance, owner):
        print(f"ReadCoordinate.__get__: {self.name}")
        return getattr(instance, self.name)


class Point3D:
    x = Coordinate()
    y = Coordinate()
    z = Coordinate()
    xr = ReadCoordinate()

    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z


pt = Point3D(1, 2, 3)
pt2 = Point3D(3, 2, 1.5)
print(pt.__dict__)
print(pt2.__dict__)
# {'_x': 1, '_y': 2, '_z': 3}
# {'_x': 3, '_y': 2, '_z': 1.5}

print(pt.xr)
# 1
