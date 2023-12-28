#9. Свойства property. Декоратор @property

class Person:
    def __init__(self, name: str, age: int, growth: int):
        self.__name = name
        self.__age = age
        self.__growth = growth

    def get_age(self):
        print("get_age")
        return self.__age

    def set_age(self, age: int):
        print("set_age")
        self.__age = age
    
    age = property(get_age, set_age)

    age2 = property()
    age2 = age2.getter(get_age)
    age2 = age2.setter(set_age)

    @property
    def growth(self):
        print("get_growth")
        return self.__growth
    
    @growth.setter
    def growth(self, growth: int):
        print("set_growth")
        self.__growth = growth

    @growth.deleter
    def growth(self):
        print("del_growth")
        del self.__growth


me = Person("Tiger", 30, 170)
me.__dict__["age"] = "attribute age in object me"
print(me.age)
# get_age
# 30

me.age = 11
# set_age

print(me.age)
# get_age
# 11

print(me.__dict__)
# {'_Person__name': 'Tiger', '_Person__age': 11,
# '_Person__growth': 170, 'age': 'attribute age in object me'}

print(me.age2)
# 11

me.growth = 171
print(me.growth)
# set_growth
# get_growth
# 171

del me.growth
print(me.__dict__)
# del_growth
# {'_Person__name': 'Tiger', '_Person__age': 11,
# 'age': 'attribute age in object me'}

me.growth = 170
print(me.__dict__)
# set_growth
# {'_Person__name': 'Tiger', '_Person__age': 11,
#  'age': 'attribute age in object me', '_Person__growth': 170}
