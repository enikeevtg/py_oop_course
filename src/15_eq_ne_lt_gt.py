#15. Методы сравнений __eq__, __ne__, __lt__, __gt__ и другие

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

    @classmethod
    def __verify_data(cls, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError("Операнд справа должен быть целым числом или \
объектом класса Clock")
        
        return other if isinstance(other, int) else other.seconds

    def __eq__(self, other):
        sc = self.__verify_data(other)
        return self.seconds == sc

    def __ne__(self, other):
        print("__ne__")
        return not self == other
    
    def __lt__(self, other):
        sc = self.__verify_data(other)
        return self.seconds < sc
    
    def __gt__(self, other):
        sc = self.__verify_data(other)
        return self.seconds > sc
    
    def __le__(self, other):
        sc = self.__verify_data(other)
        return self.seconds <= sc
    
    def __ge__(self, other):
        sc = self.__verify_data(other)
        return self.seconds >= sc

c1 = Clock(1000)
c2 = Clock(1000)
c3 = Clock(2000)
print(c1 == c2)
print(c1 == c3)
print(c1 == 1000)
# True
# False
# True

print(c1 != c2)
print(c1 != c3)
print(c1 != 1000)
# __ne__
# False
# __ne__
# True
# __ne__
# False

print(c1 < c2)
print(c1 < c3)
print(c1 < 1000)
# False
# True
# False

print(c1 > c2)
print(c1 > c3)
print(c1 > 1000)
# False
# False
# False
