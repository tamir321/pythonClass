from typing import Protocol

class MyShowProto(Protocol):
    def show(self):
        pass


class MyClass(MyShowProto):
    def show(self):
        print('Hello World!')


class MyOtherClass(MyShowProto):
    pass


def foo(o: MyShowProto):
    return o.show()

foo(MyClass())  # ok
foo(MyOtherClass())  # fails