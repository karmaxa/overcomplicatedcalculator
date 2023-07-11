import math
from decimal import Decimal


def add(val1, val2):
    return Decimal(val1) + Decimal(val2)


def sub(val2, val1):
    return Decimal(val1) - Decimal(val2)


def unsub(val):
    return 0 - Decimal(val)


def mul(val1, val2):
    return Decimal(val1) * Decimal(val2)


def div(val1, val2):
    if val2 == 0:
        raise ValueError(
            "Divizion by zero is illegal"
        )
    return Decimal(val1) / Decimal(val2)


def power(val1, val2):
    return Decimal(val1) ** Decimal(val2)


def sqrt(val):
    return math.sqrt(Decimal(val))


def root(val2, val1):
    return Decimal(val1) ** (1 / Decimal(val2))


def sin(val):
    return math.sin(Decimal(val))


def cos(val):
    return math.cos(Decimal(val))


def tan(val):
    return math.tan(Decimal(val))


def ctg(val):
    return 1 / math.tan(Decimal(val))


def arcsin(val):
    if not -1 <= val <= 1:
        raise ValueError(
            "Reverse trigonometric functions accespt only values in [-1, 1]"
        )
    return math.asin(Decimal(val))


def arccos(val):
    if not -1 <= val <= 1:
        raise ValueError(
            "Reverse trigonometric functions accespt only values in [-1, 1]"
        )
    return math.acos(Decimal(val))


def arctan(val):
    return math.atan(Decimal(val))


def arcctg(val):
    return (math.pi / 2) - math.atan(Decimal(val))


def log(val2, val1):
    return math.log(Decimal(val1), Decimal(val2))


def ln(val):
    return math.log(Decimal(val), math.e)
