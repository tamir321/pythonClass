import re

"""Define functions inside other functions """


def printHello(name):
    def message():
        return "Hello "

    result = message() + name
    return result


print(printHello("David"))

"""
Functions can be passed as parameters to other functions
Functions can return other functions
"""


def get_text(name):
    return f"long     sentence      for  {name}    ."


def squeezeSpace(func):
    def squeezer(name):
        str = func(name)
        return re.sub(r' +', '~', str)

    return squeezer


new_get_text = squeezeSpace(get_text)
print(new_get_text("John"))


@squeezeSpace
def get_text2(name):
    return f"long     sentence      for  {name}    from function  get  text 2."


print(get_text2("tamir"))

"""Passing arguments"""


def squeezer(name):
    ch = " "
    return re.sub(f"{ch}+", ch, name)


print(squeezer("long     sentence      for  {name}    from function  get  text 2."))


def squeezeChar(ch):
    def squeezeRepeat(func):
        def squeezer(name):
            str = func(name)
            return re.sub(f"{ch}+", ch, str)

        return squeezer

    return squeezeRepeat


@squeezeChar(" ")
def get_other_text(name):
    return f"long     sentence      for  {name}    from function  get  text squeezeChar."


@squeezeChar("~")
def get_other_text_2(name):
    return f"long~~~~~sentence~~~~~for~~~{name}~~~~from~~~function~get~text squeezeChar~."


print(get_other_text_2("bla bla"))
