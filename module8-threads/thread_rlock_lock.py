import threading
import time


def increment(lock):
  lock.acquire()
  time.sleep(5)
  global counter
  counter += 1
  lock.release()

def main():
  global counter
  counter = 0

  # Create a lock and an RLock
  lock = threading.Lock()
  rlock = threading.RLock()

  # Create two threads
  thread1 = threading.Thread(target=increment, args=(lock,))
  thread2 = threading.Thread(target=increment, args=(lock,))

  # Start the threads
  thread1.start()
  thread2.start()

  # Wait for the threads to finish
  thread1.join()
  thread2.join()

  # Print the value of counter
  print(counter)

if __name__ == "__main__":
  main()