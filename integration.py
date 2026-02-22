#  code in python for integration without using any library

print("enter a function of x (e.g., 'x**2 + 3*x + 2'): ")
user_input = input()
print ("enter limits of integration (lower and upper) separated by space: ")
lower, upper = map(float, input().split())
def f(x):
    return eval(user_input)

def integrate(lower, upper, segments):
    dx = (upper - lower) / segments
    total_area = 0.5 * (f(lower) + f(upper))
    
    for i in range(1, segments):
        x = lower + i * dx
        total_area += f(x)
    
    return total_area * dx

a = 0
b = 1
n = 1000

result = integrate(a, b, n)
print(result)