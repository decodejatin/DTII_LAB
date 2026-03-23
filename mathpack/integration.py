def integrate(func, lower, upper, segments=1000):
    dx = (upper - lower) / segments
    total_area = 0.5 * (func(lower) + func(upper))
    for i in range(1, segments):
        x = lower + i * dx
        total_area += func(x)
    return total_area * dx
