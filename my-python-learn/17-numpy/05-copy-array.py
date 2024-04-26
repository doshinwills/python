from numpy import *


arr1 = arange(1,10)
arr2 = arr1.view()

print("a1", arr1)
print("a2", arr2)

arr2[3] = 30
print("a1", arr1)
print("a2", arr2)

arr1 = arange(1,10)
arr2 = arr1.copy()

print("a1", arr1)
print("a2", arr2)

arr2[3] = 30
print("a1", arr1)
print("a2", arr2)
