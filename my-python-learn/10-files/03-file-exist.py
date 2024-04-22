import os.path
import sys

if os.path.isfile("data1.txt"):
    f = open("data.txt", "r")
    s = f.read()
    print(s)
    f.close()
else:
    print("File dont exists")
    sys.exit(9)