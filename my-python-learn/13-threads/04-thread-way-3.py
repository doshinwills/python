import threading

class MyClass():
    def disNums(self):
        i = 0
        while(i < 10):
            print(threading.current_thread().name, i)
            i+=1


mc = MyClass()
t = threading.Thread(target=mc.disNums)
t.start()
print(threading.current_thread().name, " started")