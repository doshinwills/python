import threading

class MyClass(threading.Thread):
    def run(self):
        i = 0
        while(i < 10):
            print(threading.current_thread().getName(), i)
            i+=1


t = MyClass()
t.start()
print(threading.current_thread().getName(), " started")