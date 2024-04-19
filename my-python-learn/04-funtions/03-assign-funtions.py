a = 10
b = 20

def printval():
    a = 50
    print(a)
    print(globals()['a'])

fun = printval

fun()
fun()
