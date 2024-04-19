class Product:
    def __init__(self, name, dis, price):
        self.__name = name
        self.__dis = dis
        self.__price = price


    def start(self):
        print("product start")

    def stop(self):
        print("product stop")


class Iphone(Product):
    def __init__(self, version, name, dis, price):
        # Option 1
        Product.__init__(self, name, dis, price)
        # Option 2
        super().__init__(name, dis, price)

        self.__version = version

    def start(self):
        print("Iphone start")
    def printVersion(self):
        super().start()
        print("Version ", self.__version)

p1 = Iphone("version", "name", "discription", 20)

print(type(p1))
# Name mangling syntax
print(p1._Product__name)

p1.start()
p1.stop()

p1.printVersion()

