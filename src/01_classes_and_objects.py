#1. Классы и объекты. Атрибуты классов и объектов

# class Point
class Point:
    """some documentation"""

    color = "red"
    size = 3


print(Point.__dict__)
# {'__module__': '__main__', '__doc__': 'some documentation', 'color': 'red', 'size': 3, '__dict__': <attribute '__dict__' of 'Point' objects>, '__weakref__': <attribute '__weakref__' of 'Point' objects>}


# Создание объектов класса Point
a = Point()
b = Point()
print("a:", a.__dict__)
print("b:", b.__dict__)
print(a.color)
# a: {}
# b: {}
# red


# Проверка типа экземпляра класса
print(type(a))
# <class '__main__.Point'>
print(isinstance(b, Point))
# True


# Добавление локального аттрибута в объект а
a.color = "green"
print(a.__dict__)
# 'color': 'green'}


# Добавление в класс нового аттрибута
Point.new_attr = "new attribute"
print(Point.__dict__)
# {'__module__': '__main__', '__doc__': 'some documentation', 'color': 'red', 'size': 3, '__dict__': <attribute '__dict__' of 'Point' objects>, '__weakref__': <attribute '__weakref__' of 'Point' objects>, 'new_attr': 'new attribute'}
setattr(Point, "new_attr_2", "second new attribute")
print(Point.__dict__)
# {'__module__': '__main__', '__doc__': 'some documentation', 'color': 'red', 'size': 3, '__dict__': <attribute '__dict__' of 'Point' objects>, '__weakref__': <attribute '__weakref__' of 'Point' objects>, 'new_attr': 'new attribute', 'new_attr_2': 'second new attribute'}


# Берём значение аттрибута класса
Point.color
get_nonexist_attribute = getattr(Point, "a", False)
print(get_nonexist_attribute)
# False


# Удаляем аттрибут из соответствующего пространства имён
if hasattr(Point, "new_attr"):
    del Point.new_attr
if hasattr(Point, "new_attr_2"):
    delattr(Point, "new_attr_2")
print(Point.__dict__)
# {'__module__': '__main__', '__doc__': 'some documentation', 'color': 'red', 'size': 3, '__dict__': <attribute '__dict__' of 'Point' objects>, '__weakref__': <attribute '__weakref__' of 'Point' objects>}
