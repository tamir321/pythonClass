import os

# os.environ['HOME']
home = os.getenv("HOME",42)
print("home is - ",home)

# os.putenv("HOME","blabla")  #- Such a changes to the environment affects the sub-processes,  created after the change
os.environ['HOME']  = "blabla"
new_home = os.getenv("HOME",7)
print(new_home)