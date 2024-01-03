import math

# Класс-декоратор для вычисления производной функции 
class Derivate:
    def __init__(self, func):
        self.__fn = func

    def __call__(self, x, dx=0.0001, *args, **kwargs):
        return (self.__fn(x + dx) - self.__fn(x)) / dx


def fn_sin(x):
    return math.sin(x)


@Derivate
def df_cos(x):
    return math.cos(x)


df = Derivate(fn_sin)
x = math.pi
print(fn_sin(x), df(x), df_cos(x), sep='\n')
# 1.2246467991473532e-16
# -0.9999999983354435
# 4.999999969612645e-05
