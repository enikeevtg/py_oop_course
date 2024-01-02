#11. Дескрипторы (data descriptor и non-data descriptor)

# Реализация без дескрипторов
class Point3D_v1:
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z

    @classmethod
    def __check_coord(cls, coord):
        if not isinstance(coord, (int, float)):
            raise TypeError("Координата должна быть числом")

    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, x):
        self.__check_coord(x)
        self._x = x

    @property
    def y(self):
        return self._y
    
    @x.setter
    def y(self, y):
        self.__check_coord(y)
        self._y = y

    @property
    def z(self):
        return self._z
    
    @x.setter
    def z(self, z):
        self.__check_coord(z)
        self._z = z
