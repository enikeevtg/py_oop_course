#4. Магический метод __new__. Пример паттерна Singleton

# singleton implementation
from typing import Any


class DataBase:
    """singleton example"""

    __instance = None
    __initialized = False

    def __new__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__new__(self)
        return self.__instance

    def __del__(self):
        DataBase.__instance = None

    def __init__(self, user, psw, port):
        if self.__initialized is False:
            self.user = user
            self.psw = psw
            self.port = port  
            self.__initialized = True          

    # def __call__(self, *args, **kwargs):
    #     if self.__instance is None:
    #         self.__new__(*args, **kwargs)
    #         self.__init__(*args, **kwargs)
    #     return self.__instance

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
# def __call__(self, *args, **kwargs):

        
