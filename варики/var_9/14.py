def f(a):
    s = ''
    while a > 0:
        s = str(a % 7) + s
        a //= 7
    return s


print(max([[f(7 ** 270 + 7 ** 170 + 7 ** 70 - x).count('0'), x] for x in range(1, 10001)], key=lambda o: (o[0], o[1]))[1])