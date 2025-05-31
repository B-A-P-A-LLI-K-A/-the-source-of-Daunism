def f(a, b):
    if a == b:
        return 1
    if a > b:
        return 0
    else:
        return f(a + 3, b) + f(a + c(a), b)


def c(r):
    ma = 0
    for i in str(r):
        if ma < int(i):
            ma = int(i)
    return ma


print(f(10, 24) * f(24, 41))
