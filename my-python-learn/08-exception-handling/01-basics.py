# main exceptions https://martinxpn.medium.com/exception-hierarchy-python-58-100-days-of-python-9d8585e6569b

try:
    a = 5
    a/0
except ZeroDivisionError:
    print("Ex")
except:
    print("All Ex")

print("-------")

try:
    f = open("myfile", "w")
    f.write("hello")
except ZeroDivisionError:
    print("Ex")
else:
    print("No exception")
finally:
    f.close()
    print("Finally")