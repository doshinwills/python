import pickle


class Student:
    def __init__(self, id, name, score):
        self.id = id
        self.name = name
        self.score = score

s = Student(1, "Doshin", 80)
f = open("student.dat", "xb+")

pickle.dump(s, f)

s = pickle.load(f)

print(s.id)

f.close()

