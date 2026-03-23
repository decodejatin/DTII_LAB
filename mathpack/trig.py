def factorial(n):
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res

def my_sin(x, terms=10):
    sine_val = 0
    for n in range(terms):
        sign = (-1)**n
        numerator = x**(2 * n + 1)
        denominator = factorial(2 * n + 1)
        sine_val += sign * (numerator / denominator)
    return sine_val

def my_cos(x, terms=10):
    x = x % (2 * 3.141592653589793)
    cos_val = 0
    for n in range(terms):
        sign = (-1)**n
        numerator = x**(2 * n)
        denominator = factorial(2 * n)
        cos_val += sign * (numerator / denominator)
    return cos_val

def my_tan(x):
    s = my_sin(x)
    c = my_cos(x)
    if c == 0:
        return float('inf')
    return s / c

def my_cot(x):
    s = my_sin(x)
    c = my_cos(x)
    if s == 0:
        return float('inf')
    return c / s

def my_sec(x):
    c = my_cos(x)
    if c == 0:
        return float('inf')
    return 1 / c

def my_csc(x):
    s = my_sin(x)
    if s == 0:
        return float('inf')
    return 1 / s
