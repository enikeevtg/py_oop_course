#39. Python Data Classes при наследовании

from dataclasses import dataclass, field, InitVar
from typing import Any


class GoodsMethodsFactory:
    @staticmethod
    def get_init_measure():
        return [0, 0, 0]


@dataclass
class Goods:
    current_uid = 0

    uid: int = field(init=False)
    price: Any = None
    weight: Any = None

    def __post_init__(self):
        print("Goods: post_init")
        Goods.current_uid += 1
        self.uid = Goods.current_uid


@dataclass
class Book(Goods):
    title: str = ""
    author: str = ""
    price: float = 0
    weight: int | float = 0
    measure: list = field(default_factory=GoodsMethodsFactory.get_init_measure)

    def __post_init__(self):
        print("Book: post_init")
        super().__post_init__()


b1 = Book()
print(b1)
# Book: post_init
# Goods: post_init
# Book(uid=1, price=0, weight=0, title='', author='', measure=[0, 0, 0])

b2 = Book()
b3 = Book()
print(b3)
# Book: post_init
# Goods: post_init
# Book: post_init
# Goods: post_init
# Book(uid=3, price=0, weight=0, title='', author='', measure=[0, 0, 0])
