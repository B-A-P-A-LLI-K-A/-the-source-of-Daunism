def f(a):
    if a == 38:
        return 1
    elif a > 38 or a == 22:
        return 0
    else:
        return f(a + 3) + f(a + 4)


print(f(16))