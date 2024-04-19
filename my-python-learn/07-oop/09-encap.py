class Product:
    def __init__(self):
        self.__name = 'iphone'
        self.__discription = 'Awesome'
        self.__price = 700


p1 = Product()

print(type(p1))
# Name mangling syntax
print(p1._Product__name)
