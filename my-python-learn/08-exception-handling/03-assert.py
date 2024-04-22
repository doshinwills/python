i = 501

try:
    assert i < 500, "Wrong input greater than 500"
except AssertionError:
    print("Assert error")

print("processing after")