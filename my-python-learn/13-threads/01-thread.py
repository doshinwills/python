import threading

print(threading.current_thread().getName())

if(threading.current_thread() == threading.main_thread()):
    print("Main thread")