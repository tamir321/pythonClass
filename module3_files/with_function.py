class my_class:

    def __init__(self, a):
        self.a = a

    def do_something(self, i):
        print("doing", self.a * i+" ")

    def __1exit__(self, exc_type, exc_val, exc_tb):
        print("\nInside __exit__")
        print("\nExecution type:", exc_type)
        print("\nExecution value:", exc_val)
        print("\nTraceback:", exc_tb)
    def __del__(self):
        print("del was here")

    def __1enter__(self):
        print("I entered the objet")
        return self   # if removed cant use the "r" in the with statment


with my_class("bla") as r:
    r.do_something("fd")
    print("I am done")




# print("out of scope")


