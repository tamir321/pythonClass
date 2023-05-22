import time
import threading

global_num =10
run_thread = True

def func():
    global global_num
    global run_thread
    #print("lets start thread")
    while run_thread:
        global_num += 1
        #print(f"Hi from thread global_num = {global_num}")
        time.sleep(2)
    #print("thread ended")

def stop_func():
    global  run_thread
    a = " "
    while a != "stop":
        print(f"currently the global_num={global_num}")
        a = input("type stop to stop: \n")
    run_thread = False

print("lets strat")

my_thread = threading.Thread(target=func,daemon=True ,name='background')
#stop_threa = threading.Thread(target=stop_func,name='stop')

#stop_threa.start()
my_thread.start()
stop_func()


#stop_threa.join()
my_thread.join()
print("end of program global_num=",global_num)

