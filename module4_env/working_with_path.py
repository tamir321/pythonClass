import os

my_path = r"C:\Users\tamir\Documents\pythonProject\module4_env"
print("os.path.dirname",os.path.dirname(my_path))
print("os.path.exists",os.path.exists(my_path))
print("os.path.isdir",os.path.isdir(my_path))
print("os.path.isfile",os.path.isfile(r"C:\Users\tamir\Documents\pythonProject\module4_env\redairect_stderr.py"))
new_path = os.path.join(my_path,"redairect_stderr.py")
print("os ptah new_path", os.path.isfile(new_path))

