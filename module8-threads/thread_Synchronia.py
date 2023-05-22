import threading
import time

lock = threading.Lock()

def start_metting(person):
    lock.acquire()
    print(f"person - {person} started the meeting in meeting room ")
    time.sleep(3)
    print(f"person - {person} finished the meeting in meeting room ")
    lock.release()
    

th1 = threading.Thread(target=start_metting,args=(1,))
th2 = threading.Thread(target=start_metting,args=(2,))

th1.start()
th2.start()

th1.join()
th2.join()
