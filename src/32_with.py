#32. Менеджеры контекстов. Оператор with

class VectorDefender:
    def __init__(self, v) -> None:
        self.__v = v

    def __enter__(self):
        self.__buf = self.__v[:]
        return self.__buf
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.__v = self.__buf[:]

        return False


v1 = [1, 2, 3]
v2 = [4, 5]

try:
    with VectorDefender(v1) as dv:
        for i, val in enumerate(dv):
            dv[i] += v2[i]
except:
    print("exception")
print(v1)
# exception
# [1, 2, 3]


try:
    with VectorDefender(v1) as dv:
        for i, val in enumerate(v1):
            v1[i] += v2[i]
except:
    print("exception")
print(v1)
# exception
# [5, 7, 3]
