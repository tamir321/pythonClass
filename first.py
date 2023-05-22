a= [9,1]
b= [9,1]
print(a is b)

print(id(a))
print(id(b))

b=a[:]

print("b =a",a is b)