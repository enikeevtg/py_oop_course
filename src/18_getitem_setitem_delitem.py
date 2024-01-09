#18. Магические методы __getitem__, __setitem__ и __delitem__ 

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)

    def __getitem__(self, key):
        if key < 0 or key >= len(self.marks):
            raise IndexError("Индекс за пределами существующего списка")
        
        return self.marks[key]
    
    def __setitem__(self, key, value):
        if not isinstance(key, int):
            raise TypeError("Ключ должен быть целым числом")
        # if key < 0 or key >= len(self.marks):
        #     raise IndexError("Индекс за пределами существующего списка")

        # if key < 0 or key >= len(self.marks):
        #     key %= len(self.marks)

        # отрицательный индекс
        if key < 0:
            key %= len(self.marks)

        # расширение списка, если индекс больше длины списка
        if key >= len(self.marks):
            offset = key - len(self.marks) + 1
            self.marks.extend([None] * offset)

        self.marks[key] = value

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError("Ключ должен быть целым числом")

        del self.marks[key]


s1 = Student("qwerty", [5, 5, 3, 4, 5])
print(s1[0])
# 5

s1[2] = 4
print(s1[2])
# 4

s1[11] = 11
print(s1.marks)
# [5, 5, 4, 4, 5, None, None, None, None, None, None, 11]

del s1[3]
print(s1.marks)
# [5, 5, 4, 5, None, None, None, None, None, None, 11]
