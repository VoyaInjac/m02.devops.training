# define your solution
def factorial(n):
    if n < 0:
        raise ValueError("n ne moze biti negativan")
    if n == 0:
        return 1
    if n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result = result * i
    return result


def fibonacci(n):
    if n < 0:
        raise ValueError("n ne moze biti negativan")
    if n == 0:
        return 0
    if n == 1:
        return 1
    a = 0
    b = 1
    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c
    return b

