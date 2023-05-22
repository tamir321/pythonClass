class B:
    def __init__(self):
        pass

    def x(self):
        print('x: B')


class C:
    def __init__(self):
        pass

    def x(self):
        print('x: C')


class D(B, C):
    pass


d = D()
d.x()
print(D.mro())
"""
https://www.educative.io/answers/what-is-mro-in-python
Method Resolution Order
MRO is a concept used in inheritance.
It is the order in which a method is searched for in a classes hierarchy
and is especially useful in Python because Python supports multiple inheritance."""
