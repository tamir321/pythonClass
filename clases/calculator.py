from enum import Enum

def is_float(element: any) -> bool:
    #If you expect None to be passed:
    if element is None:
        return False
    try:
        float(element)
        return True
    except Exception as e: #ValueError
        print(e)
        return False

class Actions(Enum):
    sum = lambda a, b: a + b
    dec = lambda a, b: a - b
    multy = lambda a, b: a * b
    diva = lambda a, b: a / b

def calc(action: Actions, *args):
    return action(*args)

# print(calc(Actions.sum, 3, 4))

def calc1(action, *args):
    return getattr(Actions, action)(*args)
    # return Actions.__dict__[action](*args)

def main():
    act = ""
    a = list(Actions.__dict__.keys())
    actions = list(filter(lambda x: x[0] != '_', a))
    while act not in Actions.__dict__.keys():
        act = input(f"Type the action you want from the list {actions} ")

    args_to_calc = [""] * 2

    for i in range(len(args_to_calc)):
        while not isinstance(args_to_calc[i], (int, float)):
            arg = input(f"insrt a number {i + 1}-")
            if is_float(arg):
                args_to_calc[i] = float(arg)

    result = calc1(act, *args_to_calc)
    print(result)


if __name__ == "__main__":
    main()