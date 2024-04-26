from numpy import *

a1 = arange(120)
print(a1)

a2 = reshape(a1, (5,4,3,2))
print(a2)

print(a2.flatten())


print(eye(4))

print(ones((2,3), int))

print(zeros((2,3), int))



