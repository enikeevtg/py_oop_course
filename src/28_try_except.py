#28. Введение в обработку исключений. Блоки try / except

try:
    f = open("notexist_file.txt")
except FileNotFoundError:
    print("file not found")

try:
    f = open("notexist_file.txt")
except FileNotFoundError:
    pass

try:
    f = open("notexist_file.txt")
except:
    pass

print("next code")
# file not found
# next code


try:
    x, y = map(int, input().split())
    res = x / y
except ValueError:
    print("Ошибка типа данных")
except Exception:
# except ArithmeticError:
# except ZeroDivisionError:
    print("Деление на ноль")
except:
    print("Ошибка")
