import types
class Dog:
    def __init__(self,name: str,age: int):
        self.name = name
        self.age = age

    def __le__(self, other):
        return self.age >= other.age

moki = Dog("Moki",12)
shoki = Dog("Shoki",25)

print(type(moki))
print(isinstance(moki,Dog))
print("moki >= shoki ",moki >= shoki)
print("moki > shoki ",moki > shoki)