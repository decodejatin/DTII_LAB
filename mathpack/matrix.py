def matrix_add(a, b):
    rows = len(a)
    cols = len(a[0])
    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(a[i][j] + b[i][j])
        result.append(row)
    return result

def matrix_sub(a, b):
    rows = len(a)
    cols = len(a[0])
    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(a[i][j] - b[i][j])
        result.append(row)
    return result

def matrix_mul(a, b):
    rows_a = len(a)
    cols_a = len(a[0])
    cols_b = len(b[0])
    result = []
    for i in range(rows_a):
        row = []
        for j in range(cols_b):
            s = 0
            for k in range(cols_a):
                s += a[i][k] * b[k][j]
            row.append(s)
        result.append(row)
    return result

def matrix_transpose(a):
    rows = len(a)
    cols = len(a[0])
    result = []
    for j in range(cols):
        row = []
        for i in range(rows):
            row.append(a[i][j])
        result.append(row)
    return result

def matrix_determinant(a):
    n = len(a)
    if n == 1:
        return a[0][0]
    if n == 2:
        return a[0][0] * a[1][1] - a[0][1] * a[1][0]
    det = 0
    for j in range(n):
        sub = []
        for i in range(1, n):
            row = []
            for k in range(n):
                if k != j:
                    row.append(a[i][k])
            sub.append(row)
        sign = 1 if j % 2 == 0 else -1
        det += sign * a[0][j] * matrix_determinant(sub)
    return det
