#34. Метаклассы. Объект type

class A:
    pass

print(type(int))
print(type(str))
print(type(A))
# <class 'type'>
# <class 'type'>
# <class 'type'>


# динамическое создание классов
B = type("Point", (), {"MAX_COORD": 100, "MIN_COORD": 0})
pt = B()
print(B)
print(pt)
# <class '__main__.Point'>
# <__main__.Point object at 0x7fdd53e8c310>

print(pt.MAX_COORD)
# 100


# наследование в динамическисоздаваемом классе
class C1: pass
class C2: pass
C = type("MetaInheritanceExample", (C1, C2), {})
print(C.__mro__)
# (<class '__main__.MetaInheritanceExample'>,
# <class '__main__.C1'>, <class '__main__.C2'>,
# <class 'object'>)


# методы в динамически созданном классе
def print_attr(self):
    print(self.__dict__)

D = type("ClassWithMethods", (), {"attr": "attribute",
                                  "print_attr": print_attr})
D().print_attr()
# {}

D = type("ClassWithMethods", (), {"attr": "attribute",
                                  "print_attr": lambda self:
                                  print(self.__dict__)})
D().print_attr()
# {}
