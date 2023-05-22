class Foo:

    def __init__(self, x):
        self.x = x


    def __del__(self):
        print("end of Foo")


foo = Foo(40)
foo = None


