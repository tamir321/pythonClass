def gen_range(n):
    i = 0
    while i < n:
        print("~gen_range~",i)
        yield i
        print("~the function did somthing~")
        i += 1
    yield  1
    yield 2


def my_gen(n):
    print(n)
    print("I was here")
    yield "tamir"
    print("I am back")
    yield "I will back"
    print("end")

test = my_gen("bla bla")

print(test.__next__())
print(test.__next__())
# for a in test:
#     z = input("123456")
#     print(f"out of function {a}")


# results  =  gen_range(5)
#
# for n in results:
#     print("result n =",n)
#     print("blabla")
#     print("blabla")
#     print("blabla")
#     print("blabla")
#
#
# print("the sum is ",sum(gen_range(10)))

# def gen(n):
#     for i in range(0,n+1):
#         yield i
#
#
# print("list(gen(6))",list(gen(6)))
# my_list = [x*2 for x in gen(7)]
# print("my_list" , my_list)
#
# def generator():
#     yield "H"
#     yield "E"
#     yield "L"
#     yield "L"
#     yield "O"
#
# test = generator()
# print("list(test)",list(test))
#
# print("list(test)",list(test))