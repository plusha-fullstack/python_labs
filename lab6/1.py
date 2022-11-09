from math import sin


def sinus():
    v = ((1 + sin(1))/3) + ((1 + sin(3))/3) + ((1 + sin(5))/3)
    return v


print(sinus())
