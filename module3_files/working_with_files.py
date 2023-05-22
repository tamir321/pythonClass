"""read as string"""
# open text file in read mode
text_file = open("doc.txt", "r")

# read whole file to a string
data = text_file.read()

# close file
text_file.close()

print(data)


"""read line by line"""
text_file = open("doc.txt", "r")
for line in text_file:
    print ("-",line)

text_file.close()

"""write to file if the """
data = ""
with open("doc.txt", "r") as read_file:
    data = read_file.read()

with open("new_file.txt", "w") as new_file:
    new_file.write(data)


"""getting file position and attributes"""
f = open("doc.txt", "r")
f.readline()
f.readline()
print(f"1@@{f.tell()}")
f.readline()
f.readline()
print(f"2@@{f.tell()}")
f.close()
print ("Name of the file: ", f.name )
print ("Closed or not : ", f.closed )
print ("Opening mode : ", f.mode)




"""appand new line"""

with open('new_file.txt', 'a') as fd:
    end_line = "~*"*20
    fd.write(f'\n{end_line}')


with open("new_file.txt", "r+") as new_file:
    new_file.write(data)