#29. Обработка исключений. Блоки finally и else

print(">>> 1 <<<")
try:
    x, y = map(int, input().split())
    res = x / y
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)
else:
    print("else: good job")
finally:
    print("finally: bad job")


print(">>> 2 <<<")
try:
    f = open("29_finally_else.py")
    f.write("hello")
except FileNotFoundError as e:
    print(e)
except BaseException as e:
    print(e)
finally:
    if f:
        f.close()
        print("file closed")
# >>> 2 <<<
# not writable
# file closed


# try-except in function
print(">>> 3 <<<")
def get_values():
    try:
        x, y = map(int, input().split())
        return x, y
    except ValueError as e:
        print(e)
        return 0, 0
    finally:
        print("finally block executed before value return")

x, y = get_values()
print(x, y)
    

# вложенные блоки try-except:
print(">>> 4 <<<")
try:
    x, y = map(int, input().split())
    try:
        res = x / y
    except ZeroDivisionError as e:
        print(e)
except ValueError as e:
    print(e)


print(">>> 5 <<<")
def div(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        print(e)

res = 0
try:
    x, y = map(int, input().split())
    res = div(x, y)
except ValueError as e:
    print(e)

print("res =", res)
