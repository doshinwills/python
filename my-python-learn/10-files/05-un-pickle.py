import pickle


class Student:
    def __init__(self, id, name, score):
        self.id = id
        self.name = name
        self.score = score

f = open("student.dat", "rb")
s = pickle.load(f)

print(s.id)

f.close()

