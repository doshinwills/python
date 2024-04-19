
lst =[1, 2, 3]

#immutablke
b = bytes(lst)
print(b[1]) #to print bytes

#mutable
ba = bytearray(lst)

print(ba) #to print bytearrays
ba[1] = 22
print(ba)

lst= list(ba)
print(lst)
