_none, _float = None, 3.78
aa , bb = (1,2)

print(f"aa= {aa}")
a = 3
_bool = True
_str = "asasas"
b = [1,2,3,4]
c = (1,3,4)
e = {"a":1,"b":3,"c":3}
d = {1,1,2,4,3,"fdhfg",(2,"t",5),c,(1,3,4)}

print(d)

for keys , value in e.items():
    print(f"key = {keys}, val = {value}")


for item in e.items():
    print(f"item = {item} type = {type(item)}")


for key in e.keys():
    print(f"key = {key}, val = {e.get(key)}  {e[key]}")


_str = "abcdefg"

print("_str[10]",type(_str[10:11]))


def my_func():
    print("a")

a = my_func()
print(type(a))


_my_str = "assaasdf"
my_lst = []

for ch in _my_str:
    my_lst.append(ch)

print(f" my_lst = {my_lst} is {type(my_lst)}")

my_lst2 = [ch for ch in _my_str]

print(f" my_lst = {my_lst2} is {type(my_lst2)}")