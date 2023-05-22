import multiprocessing as MP
import time

def func():
    for n in range(1000000000):
        pass

if __name__ == "__main__":
    p = MP.Process(target=func)
    p.start()
    p.join(1)
    while p.exitcode is None:
        print("in loop")
        p.join(1) # specifies how long the current thread is willing to wait for the target thread to terminate, in seconds


    print("p.exitcode",p.exitcode)