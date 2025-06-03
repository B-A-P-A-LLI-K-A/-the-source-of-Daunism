def f(a):
    s = ''
    while a > 0:
        s = str(a % 4) + s
        a //= 4
    return s


print(f(4 ** 644 + 4 ** 322 + 16 ** 35 - 64 ** 3).count('3'))