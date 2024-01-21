#30. Распространение исключений (propagation exceptions)

def func1():
    try:
        return 1 / 0
    except BaseException as e:
        print("func1():", e)


def func2():
    try:
        return func1()
    except BaseException as e:
        print("func2() call func1():", e)


try:
    func2()
except BaseException as e:
    print("main call func2():", e)
