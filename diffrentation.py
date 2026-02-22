h = 1e-7
x = int(input("Enter the value of x to differentiate at: "))
AssertionError = input("Enter a function of x (e.g., 'x**2 + 3*x + 2'): ")
def differentiate(func,x):
    return (func(x) - func(x - h)) / (h)
def func(x):
    return eval(AssertionError)
    
print("Derivative at x:", differentiate(func, x))    







# ==================================================================================================================================#
def factorial(n):
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res

def my_sin(x, terms=10):
    """Calculates sine using Taylor series expansion"""
    sine_val = 0
    for n in range(terms):
        sign = (-1)**n
        numerator = x**(2 * n + 1)
        denominator = factorial(2 * n + 1)
        sine_val += sign * (numerator / denominator)
    return sine_val

pi = 3.141592653589793
angle_rad = 90 * (pi / 180)

print(f"Manual Sine: {my_sin(angle_rad)}")


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

print(f"Manual Cosine: {my_cos(angle_rad)}")
print(f"Manual Tangent: {my_tan(angle_rad)}")   
print(f"Manual Cotangent: {my_cot(angle_rad)}")
print(f"Manual Secant: {my_sec(angle_rad)}")
print(f"Manual Cosecant: {my_csc(angle_rad)}")


def logarithm(x, base=10):
    if x <= 0:
        raise ValueError("Input must be greater than 0")
    if base <= 1:
        raise ValueError("Base must be greater than 1")
    
    log_val = 0
    power = 1
    while power < x:
        log_val += 1
        power *= base
    
    return log_val

print(f"Logarithm of 1000 to base 10: {logarithm(1000, 10)}")


def exponential(x, base=2):
    if base <= 0:
        raise ValueError("Base must be greater than 0")
    
    exp_val = 1
    for _ in range(int(x)):
        exp_val *= base
    
    return exp_val