a = 10
b = 20


def average():
    a = 50
    print(a)


def printval():
    a = 50
    print(a)
    print(globals()['a'])


average()

printval()
