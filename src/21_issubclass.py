#21. Функция issubclass(). Наследование от встроенных типов и от object

class Geom:
    pass


class Line(Geom):
    pass


print(Geom.__name__)
# Geom

print(issubclass(Line, Geom))
print(issubclass(Geom, Line))
# True
# False

l = Line()
print(isinstance(l, Line))
print(isinstance(l, Geom))
print(isinstance(l, object))
print(isinstance(Geom, object))
# True
# True
# True
# True

print("int", issubclass(int, object))
# int True
