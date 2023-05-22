keys = ["a","b","c","a",56]
values=[4,5,6,78,"blabla"]
dict = {keys[i]:values[i] for i in range(len(keys))}

print(dict)
print("~*"*30)
for item in dict.items():
    print(item, type(item))
    print(item[0])
print("~*"*30)
for item in dict.keys():
    print(item, type(item))

e = "www" in dict.keys()
print(e)

print(dict.get("asdas","blabla"))
# d1 = {elment: 0 for elment in ['a','b','c']}
#
# d2 = {n: n**2 for n in [10, 11, 12]}
#
# print(" d1",d1,"\n","d2",d2)

d = "djafhsdjkfhsdlkafjshdlkfajh"

def count_char(string):
    result = {}
    for ch in string:
        result[ch]= result.get(ch,0)+1
    return  result

print(count_char(d))
