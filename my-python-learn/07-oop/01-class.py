class Product:
    def __init__(self):
        self.name = 'iphone'
        self.discription = 'Awesome'
        self.price = 700


p1 = Product()

print(type(p1))
print(p1.name)

class Course:
    def __init__(self, name, ratings):
        self.name = name
        self.rating = ratings

c1 = Course("JMS", [1,2,3,4,5])
print(c1.name)