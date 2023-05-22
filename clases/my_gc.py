import gc
import time


def make_cycle():
    l = [1]
    l.append(l)
    print(l)


def main():
    collected = gc.collect()
    print(f"Garbage collector: collected {collected} objects.")
    print("Creating cycles...")
    for i in range(10):
        make_cycle()
    collected = gc.collect()
    print(f"Garbage collector: collected {collected} objects.")

#main()

import sys
# a = [1, 2, 3]
# while sys.getrefcount(a)> 0 :
#     time.sleep(10)
#     print(sys.getrefcount(a))

def make_cycle():
    l = [ ]
    l.append(l)
make_cycle()

print(sys.getrefcount(l))


