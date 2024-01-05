#14 Магические методы __add__, __sub__, __mul__, __truediv__

class Clock:
    __DAY = 86400  # число секунд в одном дне

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("Секунды должны быть целым числом")
        self.seconds = seconds % self.__DAY

    def __str__(self):
        return self.get_time()

    def get_time(self):
        s = self.seconds % 60
        m = (self.seconds // 60) % 60
        h = (self.seconds // 3600) % 24  # ?
        return f"{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}"

    @classmethod
    def __get_formatted(cls, val):
        return str(val).rjust(2, "0")

    def __add__(self, other: int):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Второе слагаемое должно быть целым числом\
или объектом класса Clock")

        if isinstance(other, Clock):
            other = other.seconds
        return Clock(self.seconds + other)

    def __radd__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Первое слагаемое должно быть целым числом\
или объектом класса Clock")
        return self + other

    def __iadd__(self, other):
        print("__iadd__")
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Слагаемое должно быть целым числом\
или объектом класса Clock")

        if isinstance(other, Clock):
            other = other.seconds
        self.seconds += other
        return self

    def __sub__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Уменьшаемое должно быть целым числом\
или объектом класса Clock")

        if isinstance(other, Clock):
            other = other.seconds
        return Clock(self.seconds - other)
    
    def __rsub__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Вычитаемое должно быть целым числом\
или объектом класса Clock")

        return self - other
    
    def __isub__(self, other):
        print("__isub__")
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Вычитаемое должно быть целым числом\
или объектом класса Clock")

        if isinstance(other, Clock):
            other = other.seconds
        self.seconds -= other
        return self

    def __mul__(self, other):
        if not isinstance(other, (int)):
            raise ArithmeticError("Второй множитель должен быть целым числом")
        
        return Clock(self.seconds * other)
    
    def __rmul__(self, other):
        if not isinstance(other, (int)):
            raise ArithmeticError("первый множитель должен быть целым числом")
        return self * other
    
    def __imul__(self, other):
        print("__imul__")
        if not isinstance(other, (int)):
            raise ArithmeticError("Множитель должен быть целым числом")
        
        self.seconds *= other
        return self

    def __truediv__(self, other):
        if not isinstance(other, (int)):
            raise ArithmeticError("Делитель должен быть целым числом")
        
        return Clock(self.seconds // other)
    
    def __rtruediv__(self, other):
        if not isinstance(other, (int)):
            raise ArithmeticError("Делимое должно быть целым числом")
        
        return other // self.seconds

    def __itruediv__(self, other):
        print("__itruediv__")
        if not isinstance(other, (int)):
            raise ArithmeticError("Делитель должен быть целым числом")
        
        self.seconds = self.seconds // other
        return self

    def __floordiv__(self, other):
        pass
    def __mod__(self, other):
        pass


# __add__
c1 = Clock(100)
print(c1.get_time())
c1 = c1 + 11
print(c1.get_time())
# 00:01:40
# 00:01:51

c2 = Clock(200)
c3 = c1 + c2
print(c3.get_time())
# 00:05:11

c4 = c1 + c2 + c3
print(c4.get_time())
# 00:10:22

c5 = 11 + c4
print(c5.get_time())
# 00:10:33

c1 += c2
print(c1.get_time())
# __iadd__
# 00:05:11


# __sub__
c1 = Clock(100)
print(c1.get_time())
c1 = c1 - 11
print(c1.get_time())
# 00:01:40
# 00:01:29

c2 = Clock(300)
c3 = c2 - c1
print(c3.get_time())
# 00:03:31

c4 = c2 - c1 - c3
print(c4.get_time())
# 00:00:00

c5 = 11 - c4
print(c5.get_time())
# 23:59:49

c1 -= c2
print(c1.get_time())
# __isub__
# 23:56:29


# __mul__
c1 = Clock(101)
c2 = c1 * 2
print(c2.get_time())
# 00:03:22

c2 = c1 * -2
print(c2.get_time())
# 23:56:38

c2 = 2 * c1
print(c2.get_time())
# 00:03:22

c2 = -2 * c1
print(c2.get_time())
# 23:56:38

c1 *= 11
print(c1.get_time())
# __imul__
# 00:18:31


# __truediv__
c1 = Clock(100)
c2 = c1 / 5
print(c2.get_time())
# 00:00:20

int1 = 1000 / c1
print(int1)
# 10

c1 /= 20
print(c1)
# __itruediv__
# 00:00:05
