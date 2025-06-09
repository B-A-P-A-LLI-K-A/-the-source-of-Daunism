def f(a, b):
    if a > b or a == 27:
        return 0
    if a == b:
        return 1
    return f(a + 3, b) + f(a + 5, b) + f(a ** 2, b)


print(f(3, 16) * f(16, 51))