#4. Магический метод __new__. Пример паттерна Singleton

# class Point
class Point:
    """some documentation"""

    def __new__(cls, *args, **kwargs):
        print("вызов метода __new__ для", str(cls))
        return super().__new__(cls)

    def __init__(self, x=0, y=0) -> None:
        print("вызов метода __init__ для", str(self))
        self.x = x
        self.y = y


pt = Point(11, 11)
print(pt.__dict__)
# вызов метода __new__ для <class '__main__.Point'>
# вызов метода __init__ для <__main__.Point object at 0x7f2579b90040>
# {'x': 11, 'y': 11}
