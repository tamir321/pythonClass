a = 5
b = [5,7]

def multy_two(num,lst):
    print("num=",num)
    print("lst=", lst)
    print("a",a)
    print("b",b)

    num = 12
    b.append("new item")
    print("after change")
    print("num=", num)
    print("lst=", lst)
    print("a", a)
    print("the old b", b)
    print("end function")
    
multy_two(a,b)

print("a=",a)
print("b=",b)


# def by_ref(my_list):
#     my_list.append("new item")
#     my_list[0]=17
#     print("in function my_list",my_list)
#
# print(b)
# by_ref(b)
# print(b)

def sum(a,b):
    return a+b

def subtraction(a,b):
    return (a-b)

def multy(a,b):
    return a*b

def calc(action,*args):
    result =  action(*args)
    print(f"The of the function: \033[4m{action.__name__}\033[0m \nFor the args {args} is {result}")
    return result

calc(sum,1,3)

