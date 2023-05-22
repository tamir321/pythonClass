

import multiprocessing as MP
import time


def func(val,queue):
    cp = MP.current_process()
    print(f"in child process name={cp.name}, pid={cp.pid}, val = {val}")
    for i in range(1,10):
        queue.put({"interval":i,"pid":cp.pid,"name":cp.name,"val":val})
        time.sleep(2)
    queue.close()
    print("child process ended")


"""
In some platform, like windows, the child process goes through the main space before executing the target function. 
"""
if __name__ == '__main__':
    cp = MP.current_process()
    queue = MP.Queue()
    p = MP.Process(target=func, args=("parms_val",queue))
    print(f"in child process name={cp.name}, pid={cp.pid}")
    p.start()
    print("wait to the end")
    p.join(1)

    print("p.is_alive()",p.is_alive())
    exit = None
    while p.is_alive():
        try:
            print("get",queue.get(timeout=1))
        except Exception as ex:
            print(ex)
        print("p.is_alive()", p.is_alive())
        p.join(1)

    p.join()
    print("p.exitcode", p.exitcode)