#25. Множественное наследование

class Goods:
    def __init__(self, name, weight, price):
        super().__init__()
        print("init Goods")
        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print(f"{self.name}, {self.weight}, {self.price}")


class MixinLog:
    ID = 0

    def __init__(self) -> None:
        print("init MixInLog")
        self.ID += 1
        self.id = self.ID

    def save_sell_log(self):
        print(f"{self.id}: товар был продан в 00:00 часов")

    def print_info(self):
        print("вызов print_info() из MixinLog")

class NoteBook(Goods, MixinLog):
    # def print_info(self):
    #     MixinLog.print_info(self)
    pass


nb = NoteBook("lenovo", 800, 34000)
nb.print_info()
MixinLog.print_info(nb)
# init Goods
# lenovo, 800, 34000
# вызов print_info() из MixinLog

nb.save_sell_log()
# 1: товар был продан в 00:00 часов

print(NoteBook.__mro__)
# (<class '__main__.NoteBook'>, <class '__main__.Goods'>,
# <class '__main__.MixInLog'>, <class 'object'>)
