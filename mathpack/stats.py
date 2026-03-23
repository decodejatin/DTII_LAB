def mean(data):
    total = 0
    for x in data:
        total += x
    return total / len(data)

def median(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    if n % 2 == 1:
        return data[n // 2]
    return (data[n // 2 - 1] + data[n // 2]) / 2

def variance(data):
    m = mean(data)
    total = 0
    for x in data:
        total += (x - m) ** 2
    return total / len(data)

def std_dev(data):
    v = variance(data)
    guess = v / 2 if v > 0 else 0
    for _ in range(100):
        if guess == 0:
            return 0
        guess = (guess + v / guess) / 2
    return guess
