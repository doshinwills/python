from numpy import *

a1 = array([1,2,3,4,5,6])
a2 = array([[1,2,3],[4,5,6]])

a3 = array([[[1,2],[4,5]], [[1,2],[4,5]]])

a4 = array([[[[1,2],[4,5]], [[1,2],[4,5]]], [[[1,2],[4,5]], [[1,2],[4,5]]]])


print('-------')
print(a1.ndim)
print(a1.shape)
print(a1)
print('-------')
print(a2.ndim)
print(a2.shape)
print(a2)
a2.shape =(3,2)
print('-------')
print(a2)
print('-------')
print(a3.ndim)
print(a3.shape)
print(a3)
print('-------')
print(a4.ndim)
print(a4.shape)
print(a4.size)
print(a4.itemsize)
print(a4.dtype)
print(a4.nbytes)


print(a4)





