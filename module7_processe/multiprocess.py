import multiprocessing as MP
import time


def func(val):
    cp = MP.current_process()
    print(f"in child process name={cp.name}, pid={cp.pid}, val = {val}")
    time.sleep(2)
    print("child process ended")

"""
In some platform, like windows, the child process goes through the main space before executing the target function. 
"""
if __name__ == '__main__':
    cp = MP.current_process()
    p = MP.Process(target=func, args=("parms_val",))
    print(f"in main process name={cp.name}, pid={cp.pid}")
    p.start()
    p.join()
    print("wait to the end")
