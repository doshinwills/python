from numpy import *


arr1 = array([1,2,3,4])
arr2 = array([10,20,30,40])

print(arr1>arr2)
print(arr1<arr2)
print(arr1==arr2)

print(any(arr1==arr2))
print(all(arr1==arr2))

print(logical_and(arr1<10, arr2>10))
print(logical_or(arr1<10, arr2>10))

print(where(arr1%2==0, arr2, 0))
print(where(arr1/arr2==0, arr1, arr2))