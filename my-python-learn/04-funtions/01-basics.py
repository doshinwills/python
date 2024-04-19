

def average(a,b):
    print((a+b)/2)

def averageReturn(a,b):
    return (a+b)/2

def sunOrDiff(a,b):
    return (a+b), (a-b)

average(10,20)

avg = averageReturn(22, 40)
print(avg)

sum,diff = sunOrDiff(22, 40)
print(sum, "  ", diff)

res1 = sunOrDiff(22, 40)
print(res1[0], "  ", res1[1])