v1=10
v2=10
v3 = 10
v4 = 11
v3 += 1
print(v1 == v2) 	# compare values, return True
print(v1 is v2) 		 # probably reference to the same object, so True
print(v3 is v4)
print(id(v3), id(v4)) 	# 30779632, 30779632

l1 = [1,2,3]
l2 = [1,2,3]
print("l1==l2",l1==l2)
print("l1 is l2",l1 is l2)
print(id(l1), id(l2))
