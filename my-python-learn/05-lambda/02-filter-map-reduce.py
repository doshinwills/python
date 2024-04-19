lst=[10,2,5,7,4,9,19,45,67,55,88]

# Fileter
result = filter(lambda x: x % 2 == 0, lst)
resultlst = list(result)
print(resultlst)

# map
result2 = map(lambda x: x*2, list(resultlst))
resultlst2 = list(result2)
print(resultlst2)

#reduce
# import only funtion
from functools import reduce
sum = reduce(lambda x,y: x+y, resultlst2)
print(sum)



