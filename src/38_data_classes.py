#38. Введение в Python Data Classes (часть 2)

from dataclasses import dataclass, field, InitVar


class Vector3D:
    def __init__(self, x: int, y:int, z: int, calc_len: bool) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.length = (x ** 2 + y ** 2 + z ** 2) ** 0.5 if calc_len else 0


@dataclass
class V3D:
    x: int = field(repr=False)
    y: int
    z: int = field(compare=False)
    calc_len: InitVar[bool] = field(default=True)
    length: float = field(init=False, compare=False, default=0)
    
    def __post_init__(self, calc_len: bool):
        if calc_len:
            self.length = (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5


v = V3D(1, 2, 3)
print(v)
# V3D(y=2, z=3, length=3.7416573867739413)


v1 = V3D(1, 2, 5)
v2 = V3D(1, 2, 0)
print(v == v2)
# True

v4 = V3D(0, 5, 15, False)
print(v4)
# V3D(y=5, z=15, length=0)
