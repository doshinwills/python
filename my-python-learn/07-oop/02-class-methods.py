class Course:
    def __init__(self, name, ratings):
        self.name
        self.rating = ratings

    def average(self):
        return sum(self.rating)/len(self.rating)


c1 = Course("JMS", [1,2,3,4,5])
print(c1.average())