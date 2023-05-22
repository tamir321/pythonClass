import multiprocessing as MP
import sys
import time


def loop(sleep ,lock):
    for i in range(10):
        with lock:
            time.sleep(sleep)
            sys.stdout.write(str(i)+" ")
            sys.stdout.write("in process ")
            sys.stdout.write(MP.current_process().name + "\n")



if __name__ == "__main__":
    lock = MP.Lock()
    MP.Process(target=loop,args=(0.0001,lock) ,name="child1").start()
    MP.Process(target=loop,args=(0.0001,lock), name="child2").start()
    loop(0.1,lock)


