def differentiate(func, x, h=1e-7):
    return (func(x + h) - func(x - h)) / (2 * h)
