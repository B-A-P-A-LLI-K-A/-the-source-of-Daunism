k = 0
for x in range(1, 200):
    s = 7 ** 666 + 7 ** 333 + 49 ** x - 343
    s7 = ''
    while s > 0:
        s7 = str(s % 7) + s7
        s //= 7
    if s7.count('6') == 49:
        print(x)
