# Tuple is immutable
# Can be used as a key in dictonery

tuple2 = (1,2,3,4,5)
tuple1 = (1,)

print(tuple2*3)

list = [10, 1.5, "test", -10, 30.5]
tpl2 = tuple(list)
print(type(tpl2))

# Append to a tuple
newtuple = tuple2+(6,)
print(newtuple)
