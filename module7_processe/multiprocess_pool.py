import time
from multiprocessing import Pool
import threading
from multiprocessing.pool import ThreadPool


def increment(number):
    print(f"I was here with number = {number}")
    time.sleep(1)
    return number + 1


if __name__ == '__main__':
    start = time.time()
    numbers = list(range(100))
    pool = ThreadPool(processes=6)
    incrementedList = pool.map(increment, numbers)
    print(incrementedList)

    end = time.time()
    print("execution Time", end-start)