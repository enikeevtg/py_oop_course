#33. Вложенные классы
# на примере работы с таблицей базы данных

class Women:
    title = "объект класса для поля title"
    photo = "объект класса для поля photo"
    ordering = "объект класса для поля ordering"

    def __init__(self, user, psw):
        self._user = user
        self._psw = psw
        self.meta = self.Meta(user + '@' + psw)

    class Meta:
        ordering = ["id"]
        # t = Women.title  # не сработает

        def __init__(self, access):
            self._access = access
            self._t = Women.title  # сработает, но не рекомендуется


print(Women.ordering)
print(Women.Meta.ordering)
# объект класса для поля ordering
# ['id']

w = Women("root", "12345")
print(w.ordering)
print(w.Meta.ordering)
# объект класса для поля ordering
# ['id']

print(w.__dict__)
print(w.meta.__dict__)
# {'_user': 'root', '_psw': '12345',
# 'meta': <__main__.Women.Meta object at 0x7fda6f1d3e80>}
# {'_access': 'root@12345', '_t': 'объект класса для поля title'}
