# Example 1
def decorfun(fun):
    def inner():
        result = fun()
        return result*2
    return inner

@decorfun
def num():
    return 5


print(num())


# Example 2
def decorfun(fun):
    def inner(n):
        result = fun(n)
        result += " How are you?"
        return result
    return inner

@decorfun
def hello(name):
    return "Hello "+name

print(hello("John"))

# Example 3 chaining
def square(func):
    def inner():
        x = func()
        return x * x

    return inner


def half(func):
    def inner():
        x = func()
        return x/2

    return inner


@square
@half
def num():
    return 10

@half
@square
def num1():
    return 10


print(num())
print(num1())