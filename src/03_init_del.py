#3. Инициализатор __init__ и финализатор __del__

# class Point
class Point:
    """some documentation"""

    color = "red"
    size = 3

    def __init__(self, x=0, y=0):
        print("вызов __init__")
        self.x = x
        self.y = y

    def __del__(self):
        print("вызов __del__")

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return (self.x, self.y)


pt = Point(1, 1)
print(pt.__dict__)
pt = "переопределённый объект"
print(pt)
# вызов __init__
# {'x': 1, 'y': 1}
# вызов __del__
# переопределённый объект
