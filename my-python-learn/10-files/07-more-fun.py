import pickle

f = open("data.txt", "a+")

f.write("Hello again\n")
print("whcih location the cursor is ", f.tell())
f.seek(0)
print(f.read())

f.close()

f = open("data.txt", "a+")

for l in f:
    print(l)

