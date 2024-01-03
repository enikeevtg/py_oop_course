#12. Магический метод __call__. Функторы и классы-декораторы

class Counter:
    def __init__(self):
        self.__count = 0

    def __call__(self, step=1, *args, **kwargs):
        print("__call__")
        self.__count += step
        return self.__count


c = Counter()
c()
c(11)
count = c()
print(count)
# __call__
# __call__
# __call__
# 13
