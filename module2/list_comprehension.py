l2 = ["ab", "cd", "xyz"]
l3 = [i*7 for i in range(1,11)]
L3 = [char for char in "python"]
l4  = [char for string in l2
                for char in string]

print("l4",l4)

lst = ["c","b","a","d"]

print("lst" , lst)
lst.reverse() # ['d', 'a', 'b', 'c'] revers the order

print("lst.reverse",lst)

lst.sort()
print("lst.sort",lst)

item = ["some sting ",4,56,"other string"]

jnk = [j+1 if type(j) in(int,float) else j for j in item]

print("item",jnk)



# Create list with numbers
numbers = [2, 4, 1, 6, 3]
print("Original:",numbers)

# Using sort() with lambda
numbers.sort(key=lambda x:1/x)
print("Sorted by 1/x:",numbers)


numbers.sort(key=lambda x:x)
print("Sorted ",numbers)


strings = ["sdfsd","wew","wewe","zz","sdasd","34","1"]
strings.sort()
print("strings.sort",strings)
strings.sort(key = lambda x : len(x))
print("strings sort by lenth",strings)