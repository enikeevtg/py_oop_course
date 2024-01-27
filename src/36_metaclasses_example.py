#36. Метаклассы в API ORM Django

class Meta(type):
    def create_local_attrs(self, *args, **kwargs):
        for key, value in self.class_attrs.items():
            self.__dict__[key] = value

    def __init__(cls, name, base, attrs):
        cls.class_attrs = attrs
        cls.__init__ = Meta.create_local_attrs


class Women(metaclass=Meta):
    title = "заголовок"
    content = "контент"
    photo = "путь к фото"


w = Women(title=5)
print(w.__dict__)
# {'__module__': '__main__', '__qualname__': 'Women',
# 'title': 'заголовок', 'content': 'контент',
# 'photo': 'путь к фото'}



# мой эксперимент
class Men:
    title = "заголовок"
    content = "контент"
    photo = "путь к фото"

    def __init__(self):
        for key, value in Men.__dict__.items():
            self.__dict__[key] = value


m = Men()
print(m.__dict__)
# {'__module__': '__main__', 'title': 'заголовок', 'content': 'контент', 'photo': 'путь к фото', '__init__': <function Men.__init__ at 0x7fc7e24e7d90>, '__dict__': <attribute '__dict__' of 'Men' objects>, '__weakref__': <attribute '__weakref__' of 'Men' objects>, '__doc__': None}
