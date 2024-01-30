#39. Python Data Classes при наследовании

from dataclasses import make_dataclass, field, dataclass

class Car:
    def __init__(self, model, max_speed, price):
        self.model = model
        self.max_speed = max_speed
        self.price = price

    def get_max_speed(self):
        return self.max_speed


CarData = make_dataclass("CarData", [("model", str),
                                     "max_speed",
                                     ("price", float, field(default=0))],
                          namespace={"get_max_speed": lambda self:
                                     self.max_speed})


c = CarData("Lada", 240, 600000)
print(c)
# CarData(model='Lada', max_speed=240, price=600000)

print(c.get_max_speed())
# 240
