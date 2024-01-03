# Класс функтора, обрабатывающего строку, приходящую аргументом
# при вызове объекта
class StripChars:
    def __init__(self, chars):
        self.__chars = chars

    def __call__(self, *args, **kwargs):
        if not isinstance(args[0], str):
            raise TypeError("Аргумент должен быть строкой")
        
        return args[0].strip(self.__chars)


s1 = StripChars("* ")
s2 = StripChars("*")
res1 = s1("* * * qwertgfvdsertr * * *")
res2 = s2("* * * qwertgfvdsertr * * *")
print(res1, res2, sep = '\n')
# qwertgfvdsertr
#  * * qwertgfvdsertr * * 
