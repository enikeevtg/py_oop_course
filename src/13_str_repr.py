#13. Магические методы __str__, __repr__, __len__, __abs__

class Cat:
    def __init__(self, name):
        self.name = name

    def __repr__(self) -> str:
        """Вывод информации об объекте класса в режиме отладки"""
        return f"{self.__class__}: {self.name}"

    def __str__(self) -> str:
        """Вывод информации об объекте для пользователя"""
        return f"{self.name}"


cat = Cat("Васька")
print(repr(cat))
print(str(cat))
# <class '__main__.Cat'>: Васька
# Васька
