def poly_eval(coeffs, x):
    result = 0
    n = len(coeffs) - 1
    for i in range(len(coeffs)):
        power = n - i
        term = coeffs[i]
        for _ in range(power):
            term *= x
        result += term
    return result

def poly_add(a, b):
    if len(a) < len(b):
        a, b = b, a
    result = list(a)
    diff = len(a) - len(b)
    for i in range(len(b)):
        result[i + diff] += b[i]
    return result

def poly_multiply(a, b):
    result = [0] * (len(a) + len(b) - 1)
    for i in range(len(a)):
        for j in range(len(b)):
            result[i + j] += a[i] * b[j]
    return result
