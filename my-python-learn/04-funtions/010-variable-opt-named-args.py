# args are tupple
# kwargs is a dict
def fun(a, *args, **kwargs):
    print(a)
    print(args)
    print(kwargs)

    fun2(*args, **kwargs)


def fun2(*args, **kwargs):
    print("-----")
    print(args)
    print(kwargs)

fun(10)
fun(1,2,3,4, name="Doshin", sal=1000)
