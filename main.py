actions = {"+": (lambda a, b: a + b),
           "*": (lambda a, b: a * b),
           "/": (lambda a, b: a / b),
           "-": (lambda a, b: a - b)}

def calculator(func, a, b):
    result = func(a, b)
    print("result=", result)

calculator(actions["+"],5,4)
