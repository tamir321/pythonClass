dic = {"name":"tamir","age":3,"lastname":"Reiss"}

dic["a"]=8

print(dic)



print(dic.keys())
print(dic.values())
print(dic.items())

for key, val in dic.items():
    print(f"key = {key} , val ={val}")

for key in dic.keys():
    print(f"key = {key} , val ={dic[key]}")
print(dic.get("stam"))
print(dic.get("stam","no stam "))