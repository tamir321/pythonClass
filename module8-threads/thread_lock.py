import threading
import time

mutex = threading.Lock()
tamir_lock = threading.Lock()
shared_data = 0
shared_data2 = 0

def thread_function():
    global shared_data

    mutex.acquire()
    time.sleep(5)
    shared_data += 1  # Perform a write operation on the shared data
    mutex.release()


def thread_function_2():
    global shared_data2
    print("I was here")
    tamir_lock.acquire()
    print("start function2")
    shared_data2 += 1  # Perform a write operation on the shared data
    tamir_lock.release()

threads = []
# for _ in range(2):
#     t = threading.Thread(target=thread_function)
#     threads.append(t)
#     t.start()
t = threading.Thread(target=thread_function)
t.start()
t2 = threading.Thread(target=thread_function_2)
t2.start()

t.join()
t2.join()

print("Final value of shared_data:", shared_data)