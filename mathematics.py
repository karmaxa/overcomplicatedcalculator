import math


def add(val1, val2):
    return val1 + val2


def sub(val2, val1):
    return val1 - val2


def unsub(val):
    return 0 - val


def mul(val1, val2):
    return val1 * val2


def div(val1, val2):
    return val1 / val2


def power(val1, val2):
    return val1 ** val2


def sqrt(val):
    return math.sqrt(val)


def root(val2, val1):
    return val1 ** (1 / val2)


def sin(val):
    return math.sin(val)


def cos(val):
    return math.cos(val)


def tan(val):
    return math.tan(val)


def ctg(val):
    return 1 / math.tan(val)


def arcsin(val):
    return math.asin(val)


def arccos(val):
    return math.acos(val)


def arctan(val):
    return math.atan(val)


def arcctg(val):
    return (math.pi / 2) - math.atan(val)


def log(val2, val1):
    return math.log(val1, val2)


def ln(val):
    return math.log(val, math.e)
