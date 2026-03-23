def bisection(func, a, b, tol=1e-7, max_iter=1000):
    if func(a) * func(b) > 0:
        raise ValueError("f(a) and f(b) must have opposite signs")
    for _ in range(max_iter):
        mid = (a + b) / 2
        if func(mid) == 0 or (b - a) / 2 < tol:
            return mid
        if func(a) * func(mid) < 0:
            b = mid
        else:
            a = mid
    return (a + b) / 2

def newton_raphson(func, x0, tol=1e-7, max_iter=1000, h=1e-7):
    x = x0
    for _ in range(max_iter):
        fx = func(x)
        dfx = (func(x + h) - func(x - h)) / (2 * h)
        if dfx == 0:
            raise ValueError("Zero derivative encountered")
        x_new = x - fx / dfx
        if (x_new - x) ** 2 < tol ** 2:
            return x_new
        x = x_new
    return x
