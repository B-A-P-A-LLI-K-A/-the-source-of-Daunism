import sys
sys.setrecursionlimit(10 ** 5)
sys.set_int_max_str_digits(10 ** 7)
def f(n):
    if n == 1:
        return 1
    else:
        return (3 * n - 2) * f(n - 1)


print(int((f(10105) // 7 + f(10104)) / f(10103)))