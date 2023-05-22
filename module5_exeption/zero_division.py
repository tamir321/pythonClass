try:
    1 / 0
except ZeroDivisionError:
    print("You can't divide by zero")

print("~*" * 20)

try:
    1 / 0
except Exception as er:
    print(er)
    print("args", er.args)
    print("type er", type(er))

print("~+" * 20)

try:
    print(val + 10)
except NameError as ne:
    print("fhfhfh")
    print(ne)
except ZeroDivisionError:
    print("bla bla ")
finally:
    print("I know where you been")


class MyExection(Exception):
    def __init__(self,message,errors):
        super().__init__(message)
        self.errors = errors
    def __str__(self):
        return f"{super.__str__(self)}, error is {self.errors}"


a = 0

try:
    if a==0:
        raise MyExection("a should not be zero","not a goog error")
except MyExection as er:
    print(er)