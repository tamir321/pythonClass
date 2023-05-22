import re
my_lam = lambda x: x ** 2
my_lam2 = lambda x: [i * 2 for i in range(0, x)]
print(my_lam2(10))
lst_1 = my_lam2(10)

aaaa = lambda my_args : tuple([ i * 2 for i in my_args])
print(" aaaa -", aaaa((1,2,3)))

filterd = filter(lambda x: x % 3 == 0, lst_1)
print("filterd",filterd)
for val in filterd:
    print(val)
filterd_list = list(filter(lambda x: x % 3 == 0, lst_1))

maped = map(lambda x: f"hello {x * 2}", lst_1)
print(maped)

for val in maped:
    print(val)


maped_lst = list(map(lambda x: f"hello {x * 2}", lst_1))
print("maped_lst " , maped_lst)

a = pow(2, 5)
print(a % 10)

a = pow(2, 5, 10)
print(a)

print(list(map(pow, [2, 3, 4], [10, 5, 1, 3])))


def my_sum(a, b):
    _str = f"my sum is {a + b}"
    return _str


print(list(map(my_sum, [6, 6, 6, 6], [1, 2, 3, 4, 5, 6, 7])))

# string = "  hello    world    ,      python, aa   bbb     c,    hi  bye"
# twoWordStrsCollection = filter(lambda s: re.search("^\w+\s+\w+$", s.strip()), string.split(","))
# print(twoWordStrsCollection)
#
# print("aa bb cc".strip())

