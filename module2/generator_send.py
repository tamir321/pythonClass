def gen(num):
    i=0
    while i<=num:
        a = yield i
        print(f"when i = {i} a = {a}")
        i +=1


genereted = gen(10)
genereted.__next__()
for item in range(10):
    got_from_gen = genereted.send(f"returned value for i = {item} is {6 * 2}")
    print("got_from_gen" , got_from_gen)


