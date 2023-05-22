def gen_range(n):
    i = 0
    while i < n:
        print(" gen_range",i)
        yield i
        print(" the function did somthing")
        i += 1


results  =  gen_range(5)

for n in results:
    print("result n =",n)

def gen(n):
    for i in range(0,n+1):
        a= yield i
        print("a-", a)

print("the sum is ",sum(gen(10)))

print("list(gen(6))",list(gen(6)))
my_list = [x*2 for x in gen(7)]
print("my_list" , my_list)

def generator():
    yield "H"
    yield "E"
    yield "L"
    yield "L"
    yield "O"

test = generator()
print("list(test)",list(test))
for i in test:
    print(i)

print("list(test)",list(test))