s=input("Enter name: ")
print(s)

a=int(input("Enter age: "))
print(a)

lst = [x for x in input("Enter 3 numbers: ").split()]
print(lst)


lst = [x for x in input("Enter 3 numbers: ").split(",")]
print(lst)



a,b,c = [int(x) for x in input("Enter 3 numbers: ").split(",")]
print((a+b+c)/3)

l1 = eval(input("List of eleements")) # [1,2,3,4,5]
print(l1)