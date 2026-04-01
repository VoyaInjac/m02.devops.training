def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Ne moze se deliti sa nulom")
    return a / b


def power(a, b):
    if b < 0:
        raise ValueError("Eksponent ne moze biti negativan")
    return a ** b


def modulo(a, b):
    if b == 0:
        raise ValueError("Delilac ne moze biti nula")
    return a % b
