#10. Пример использования объектов property
from string import ascii_letters

class Person:
    RUS_LETTERS = "абвгдеёжзиклмнопрстуфхцчшщъыьэюя"
    RUS_UPPER_LETTERS = RUS_LETTERS.upper()

    # def __init__(self, fio, age, ps, weight):
    #     self.__check_fio(fio)
    #     self.__check_age(age)
    #     self.__check_passport(ps)
    #     self.__check_weight(weight)

    #     self.__fio = fio.split()
    #     self.__age = age
    #     self.__passport = ps
    #     self.__weight = weight

    def __init__(self, fio, age, ps, weight):
        self.fio = fio
        self.age = age
        self.passport = ps
        self.weight = weight

    @classmethod
    def __check_fio(cls, fio: str):
        if not isinstance(fio, str):
            raise TypeError("Данные ФИО должны быть строкой")

        fio_list = fio.split()
        if len(fio_list) != 3:
            raise TypeError("Неверный формат ФИО")
      
        letters = ascii_letters + cls.RUS_LETTERS + cls.RUS_UPPER_LETTERS
        for el in fio_list:
            if len(el) < 1:
                raise TypeError("В ФИО должен быть хотя бы один символ")
            if len(el.strip(letters)) != 0:
                raise TypeError("В ФИО допустимы только буквенные\
                                 символы и дефис")

    @classmethod
    def __check_age(cls, age):
        if not isinstance(age, int) or age < 14 or age > 120:
            raise TypeError("Возраст должен быть целым числом в диапазоне\
                            от 14 до 120")
        
    @classmethod
    def __check_weight(cls, weight):
        if not isinstance(weight, (float, int)) or weight < 20:
            raise TypeError("Вес должен быть числом от 20 кг")

    @classmethod
    def __check_passport(cls, ps):
        if not isinstance(ps, str):
            raise TypeError("Паспортные данные должны быть строкой")
        
        ps_list = ps.split()
        if len(ps_list) != 2 or len(ps_list[0]) != 4 or len(ps_list[1]) != 6:
            raise TypeError("Неверный формат паспортных данных")

        for el in ps_list:
            if not el.isdigit():
                raise TypeError("Серия и номер паспорта должны быть числами")

    # getters and setters
    @property
    def fio(self):
        return self.__fio

    @fio.setter
    def fio(self, fio):
        self.__check_fio(fio)
        self.__fio = fio.split()

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__check_age(age)
        self.__age = age

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.__check_weight(weight)
        self.__weight = weight

    @property
    def passport(self):
        return self.__passport

    @passport.setter
    def passport(self, ps):
        self.__check_passport(ps)
        self.__passport = ps


p = Person("Ыпва Дваим Жориывич", 45, "3215 795842", 68)
p.age = 18
print(p.__dict__)
