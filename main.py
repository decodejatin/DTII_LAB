from mathpack.basic import calculator
from mathpack.differentiation import differentiate
from mathpack.integration import integrate
from mathpack.trig import my_sin, my_cos, my_tan, my_cot, my_sec, my_csc
from mathpack.matrix import matrix_add, matrix_sub, matrix_mul, matrix_transpose, matrix_determinant
from mathpack.stats import mean, median, variance, std_dev
from mathpack.roots import bisection, newton_raphson
from mathpack.polynomial import poly_eval, poly_add, poly_multiply

PI = 3.141592653589793

def read_matrix(name):
    rows = int(input("Enter number of rows for " + name + ": "))
    cols = int(input("Enter number of cols for " + name + ": "))
    mat = []
    for i in range(rows):
        row = []
        for j in range(cols):
            val = float(input(name + "[" + str(i) + "][" + str(j) + "]: "))
            row.append(val)
        mat.append(row)
    return mat

def print_matrix(mat):
    for row in mat:
        line = ""
        for val in row:
            line += str(val) + "\t"
        print(line)

def main():
    while True:
        print("\n===== CALCULATOR =====")
        print("1. Basic Arithmetic")
        print("2. Differentiation")
        print("3. Integration")
        print("4. Trigonometry")
        print("5. Matrix Operations")
        print("6. Statistics")
        print("7. Root Finding")
        print("8. Polynomial Operations")
        print("9. Exit")
        choice = input("Choose: ")

        if choice == "1":
            expr = input("Enter expression (e.g. 3 + 5 * 2): ")
            tokens = expr.split()
            print("Result:", calculator(tokens))

        elif choice == "2":
            func_str = input("Enter f(x) (e.g. x**2 + 3*x): ")
            x_val = float(input("Enter x value: "))
            f = lambda x, fs=func_str: eval(fs)
            print("f'(" + str(x_val) + ") =", differentiate(f, x_val))

        elif choice == "3":
            func_str = input("Enter f(x) (e.g. x**2 + 3*x): ")
            a = float(input("Lower limit: "))
            b = float(input("Upper limit: "))
            f = lambda x, fs=func_str: eval(fs)
            print("Integral =", integrate(f, a, b))

        elif choice == "4":
            angle = float(input("Enter angle in degrees: "))
            rad = angle * (PI / 180)
            print("sin =", my_sin(rad))
            print("cos =", my_cos(rad))
            print("tan =", my_tan(rad))
            print("cot =", my_cot(rad))
            print("sec =", my_sec(rad))
            print("csc =", my_csc(rad))

        elif choice == "5":
            print("a) Add  b) Subtract  c) Multiply  d) Transpose  e) Determinant")
            op = input("Choose: ").lower()
            if op in ("a", "b", "c"):
                A = read_matrix("A")
                B = read_matrix("B")
                if op == "a":
                    print_matrix(matrix_add(A, B))
                elif op == "b":
                    print_matrix(matrix_sub(A, B))
                else:
                    print_matrix(matrix_mul(A, B))
            elif op == "d":
                A = read_matrix("A")
                print_matrix(matrix_transpose(A))
            elif op == "e":
                A = read_matrix("A")
                print("Determinant =", matrix_determinant(A))

        elif choice == "6":
            data = input("Enter numbers separated by spaces: ").split()
            data = [float(x) for x in data]
            print("Mean =", mean(data))
            print("Median =", median(data))
            print("Variance =", variance(data))
            print("Std Dev =", std_dev(data))

        elif choice == "7":
            func_str = input("Enter f(x) (e.g. x**2 - 4): ")
            f = lambda x, fs=func_str: eval(fs)
            print("a) Bisection  b) Newton-Raphson")
            method = input("Choose: ").lower()
            if method == "a":
                a = float(input("Left bound: "))
                b = float(input("Right bound: "))
                print("Root =", bisection(f, a, b))
            elif method == "b":
                x0 = float(input("Initial guess: "))
                print("Root =", newton_raphson(f, x0))

        elif choice == "8":
            print("Coefficients are highest degree first")
            print("a) Evaluate  b) Add  c) Multiply")
            op = input("Choose: ").lower()
            if op == "a":
                coeffs = [float(c) for c in input("Coefficients (e.g. 1 0 -4 for x^2-4): ").split()]
                x = float(input("x value: "))
                print("Result =", poly_eval(coeffs, x))
            elif op == "b":
                a = [float(c) for c in input("Poly A coefficients: ").split()]
                b = [float(c) for c in input("Poly B coefficients: ").split()]
                print("Sum =", poly_add(a, b))
            elif op == "c":
                a = [float(c) for c in input("Poly A coefficients: ").split()]
                b = [float(c) for c in input("Poly B coefficients: ").split()]
                print("Product =", poly_multiply(a, b))

        elif choice == "9":
            break

main()
