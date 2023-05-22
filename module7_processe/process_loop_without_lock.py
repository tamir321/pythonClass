import multiprocessing as MP
import sys
import time


def loop(sleep ):
    for i in range(40):
        time.sleep(sleep)
        sys.stdout.write(str(i)+" ")
        sys.stdout.write("in process ")
        sys.stdout.write(MP.current_process().name + "\n")



if __name__ == "__main__":
    MP.Process(target=loop,args=(0.0001,) ,name="child1").start()
    MP.Process(target=loop,args=(0.0001,), name="child2").start()
    loop(0.0001)


