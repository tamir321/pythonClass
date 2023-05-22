s1 = {1,2,3,5,6}
s2 =  {1,2,3}
s4 = {"e",7,9,3,6,1}
print(s2.issubset(s1)) # does s2 is sub set of s1
print(s1.issuperset(s2)) # does s1 contain s2

s3 = s1.union(s4)
print("s3",s3)

common = s4.intersection(s1)
print("common",common)

diff = s4.difference(s1) #set with elements in either s1 or s4 but not both
print("diff",diff)

symme = s4.symmetric_difference(s1) #set with elements in either s1 or s4 but not both
print("symme",symme)