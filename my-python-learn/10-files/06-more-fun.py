import pickle

f = open("data.txt", "r")
print(f.read())

f.seek(0)

print(f.readline())

print(f.readlines())

f.close()

