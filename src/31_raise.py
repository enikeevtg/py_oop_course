#31. Инструкция raise и пользовательские исключения

# raise ZeroDivisionError("Деление на ноль")
# e = ZeroDivisionError("Деление на ноль")
# raise e


class ExceptionPrint(Exception):
    """Общий класс исключения"""


class ExceptionPrintSendData(ExceptionPrint):
    """Класс исключения при отправке данных принтеру"""

    def __init__(self, *args):
        self.message = args[0] if args else None

    def __str__(self):
        return(f"Ошибка: {self.message}")


class PrintData:
    def print(self, data):
        self.send_data(data)
        print(f"Печать: {data}")

    def send_data(self, data):
        if not self.send_to_print():
            # raise ExceptionPrintSendData
            raise ExceptionPrintSendData("Принтер не отвечает")

    def send_to_print(self):
        return False


p = PrintData()
try:
    p.print("qwerty")
except ExceptionPrintSendData as e:
    print(e)
except ExceptionPrint as e:
    print(e)
