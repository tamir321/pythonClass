a =10
b = [1,2,3]
def add_to_a(test):
    # global a
    test = test+ 1
    print(test)

def add_to_b(lst):
    lst.append("dasd")


add_to_a(a)
print("after",a)

add_to_b(b)
print(b)



