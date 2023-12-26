#7. Магические методы __setattr__, __getattribute__, __getattr__ и __delattr__

from typing import Any


class Point:
    MAX_COORD = 100
    MIN_COORD = 0

    @classmethod
    def __check_coord(cls, x, y):
        return (cls.MIN_COORD <= x <= cls.MAX_COORD and
                cls.MIN_COORD <= y <= cls.MAX_COORD)

    @classmethod
    def tmp(cls):
        cls.__check_coord(1, 1)

    def __init__(self, x=0, y=0):
        self.x = 0
        self.y = 0
        if self.__check_coord(x, y):
            self.x = x
            self.y = y

    def get_coord(self):
        return self.x, self.y

    def __getattribute__(self, __name: str) -> Any:
        print(f"__getattribute__ {__name}")
        if __name == "__x":
            raise ValueError("access denied")
        return object.__getattribute__(self, __name)

    def __setattr__(self, __name: str, __value: Any) -> None:
        print(f"setattr {__name}")
        if __name == "z":
            raise AttributeError("wrong attribute name")
        else:
            object.__setattr__(self, __name, __value)
            
            # quick tip:
            # self.x = __value  # infinite recursion
            # self.__dict__[__name] = __value  # good, but object.__setattr__
                                               # is better

    def __getattr__(self, __name):
        print(f"__getattr__ {__name}")
        return False

    def __delattr__(self, __name: str) -> None:
        print(f"__delattr__ {__name}")
        object.__delattr__(self, __name)


pt = Point(11, 11)
print(pt.get_coord())
# setattr x
# setattr y
# __getattribute__ _Point__check_coord
# setattr x
# setattr y
# __getattribute__ get_coord
# __getattribute__ x
# __getattribute__ y
# (11, 11)


print(pt.xx)
# __getattribute__ xx
# __getattr__ xx
# False


del pt.x
print(pt.__dict__)
# __delattr__ x
# __getattribute__ __dict__
# {'y': 11}


pt.z = 1
# setattr z
# Traceback (most recent call last):
#   File "/home/tagir/Code/PY/py_course/src/07_set_get_del_attr.py", line 43, in <module>
#     pt.z = 1
#   File "/home/tagir/Code/PY/py_course/src/07_set_get_del_attr.py", line 38, in __setattr__
#     raise AttributeError("wrong attribute name")
# AttributeError: wrong attribute name
