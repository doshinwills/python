import threading, time, random

def disNums():
    i = 0
    while(i < 10):
        print(threading.current_thread().name, i)
        i+=1


t = threading.Thread(target=disNums)
t.start()

t = threading.Thread(target=disNums)
t.start()

t = threading.Thread(target=disNums)
t.start()
print(threading.current_thread().name, " started")