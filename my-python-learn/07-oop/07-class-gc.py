class Product:
    def __init__(self):
        self.name = 'iphone'
        self.discription = 'Awesome'
        self.price = 700

    def __del__(self):
        print("GC called")

p1 = Product()
p2 = Product()
p1=None
p2=None