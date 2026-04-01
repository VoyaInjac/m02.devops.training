import math


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


def power(base, exponent):
    return base ** exponent


def square_root(n):
    if n < 0:
        raise ValueError("Ne moze se koreniti negativan broj")
    return math.sqrt(n)


def modulo(a, b):
    if b == 0:
        raise ValueError("Delilac ne moze biti nula")
    return a % b


def is_even(n):
    return n % 2 == 0


def is_positive(n):
    return n > 0


def factorial(n):
    if n < 0:
        raise ValueError("n ne moze biti negativan")
    if n == 0:
        return 1
    result = 1
    for i in range(2, n + 1):
        result = result * i
    return result
