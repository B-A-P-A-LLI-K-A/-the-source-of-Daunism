def f(a):
    s = ''
    while a > 0:
        s = str(a % 3) + s
        a //= 3
    return s


k = 3 ** 68
for x in range(2005, 0, -1):
    if f(k - x).count('1') == 2:
        print(x)
        break