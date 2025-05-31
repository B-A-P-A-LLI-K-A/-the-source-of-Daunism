import sys
sys.setrecursionlimit(9999)
def f(n):
    if n <= 5:
        return 1
    else:
        return (n + f(n - 2))


print(f(2126) - f(2122))