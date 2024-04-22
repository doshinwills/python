import time, datetime

epochtime = time.time()
print(epochtime)

t = time.ctime(epochtime)
print(t)

dt = datetime.datetime.today()
print(dt)
print(dt.day, dt.month, dt.year)
print(dt.hour, dt.minute, dt.second)

d = datetime.date(2018, 7, 21)
print(d)
t = datetime.time(12, 45)
print(t)

dt = datetime.datetime.combine(d, t)
print(dt)