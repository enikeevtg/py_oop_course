#37. Введение в Python Data Classes (часть 1)

from dataclasses import dataclass, field
from pprint import pprint

class Thing:
    def __init__(self, name, weight, price, dims=[]):
        self.name = name
        self.weight = weight
        self.price = price
        self.dims = dims
    
    def __repr__(self) -> str:
        return f"Thing {self.__dict__}"
    

@dataclass
class ThingData:
    name: str
    weight: int
    price: float = 0
    dims: list = field(default_factory=list)

    def __eq__(self, __value: object) -> bool:
        """если хоти сравнивать по отдельному атрибуту"""
        return self.weight == __value.weight


t = Thing("Max+", 100, 500)
td = ThingData("Max+", 100, 500)
print(t, td, sep='\n')
# Thing {'name': 'Max+', 'weight': 100, 'price': 500, 'dims': []}
# ThingData(name='Max+', weight=100, price=500, dims=[])

# pprint(ThingData.__dict__)

td_2 = ThingData("book", 80, 100)
td_3 = ThingData("book", 80, 100)
print(td == td_2)
print(td_2 == td_3)
# False
# True

td_4 = ThingData("book", 80)
print(td_4)
# ThingData(name='book', weight=80, price=0, dims=[])


# изменяемые объекты в атрибутах класса
t.dims.append(10)
t1 = Thing(name='book', weight=80, price=0)
print(t, t1, sep='\n')
# Thing {'name': 'Max+', 'weight': 100, 'price': 500, 'dims': [10]}
# Thing {'name': 'book', 'weight': 80, 'price': 0, 'dims': [10]}

td_5 = ThingData("car", 3500000, 400000)
td_6 = ThingData("car", 4000000, 500000)
td_5.dims.append(10)
print(td_5, td_6, sep='\n')
# ThingData(name='car', weight=3500000, price=400000, dims=[10])
# ThingData(name='car', weight=4000000, price=500000, dims=[])
