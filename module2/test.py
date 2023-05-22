import time
import sys
a = [1, 2, 3]
def blabla():
    # global a
    ddddd = 8
    # print("in function a",a)
    # print("in function ggg",sys.getrefcount(ddddd))
#blabla()
print("a" , a)
print(sys.getrefcount(a))

# while sys.getrefcount(a)> 0 :
#     time.sleep(10)
#     print(sys.getrefcount(a))