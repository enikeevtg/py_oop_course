#4. Магический метод __new__. Пример паттерна Singleton

# singleton implementation
from typing import Any


class DataBase:
    """singleton example"""

    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        DataBase.__instance = None

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f"соедниние с БД: {self.user}, {self.psw}, {self.port}")

    def close(self):
        print("закрытие соединения с БД")

    def read(self):
        return "данные из БД"

    def write(self, data):
        print(f"запись в БД {data}")


db = DataBase("root", "qwerty", 80)
db2 = DataBase("user", "1234", 11)
print(db == db2)
db.connect()
db2.connect()
# True
# соедниние с БД: user, 1234, 11
# соедниние с БД: user, 1234, 11
# нужно добавлять реализацию магического метода
# def __call__(self, *args, **kwargs)
        
