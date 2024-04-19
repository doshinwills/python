# Only unique

s={10,20,"test"}
print(s)
print(type(s))

s.update([20,99])
print(s)

s.remove(20)
print(s)

# Frozon set
f = frozenset(s)
