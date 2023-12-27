#8. Паттерн "Моносостояние"

class Monostate:
    __shared_data = {}

    def __init__(self):
        self.__dict__ = self.__shared_data


def is_int(val: str) -> bool:
    try:
        int(val)
    except ValueError:
        return False
    else:
        return True


print(is_int("123.2"))

m1 = Monostate()
m1.x = 11
m2 = Monostate()
m2.y = 0
print(m1.__dict__)
print(m2.__dict__)
# {'x': 11, 'y': 0}
# {'x': 11, 'y': 0}
