import random

# Is mutable
# Can not be used as a key in dictonery
list = [10, 1.5, "test", -10, 30.5]
print(list)
print(list[3:5])
print(list*3)
print(len(list))


list.append(40)
print(list)

list.remove(-10)
print(list)

del list[2] # del(list[1])
print(list)

print("Test")
print(max(list))
print(min(list))

list.insert(10, 99)
print(list)


list.sort()
print(list)

list.sort(reverse=True)
print(list)

# randomly poicks an element from list
print(random.choice(list));

# List comprihension, list from a a list
list2 = [x**3 for x in range(1,11)]
print(list2)

# List comprihension, filter input
list2 = [x**3 for x in range(1,11) if x%2 == 0]
print(list2)

list3 = [list2[x]*list[x] for x in range(len(list2)) if x%2 == 0]
print(list3)


a = [1,2,3,4,5,6]
b = [2,5,7,8,9,10]
list4 = [i for i in a if i in b]
print(list4)

list.clear()
print(list)

