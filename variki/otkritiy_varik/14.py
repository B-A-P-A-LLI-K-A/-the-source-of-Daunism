for x in range(2300, 0, -1):
    s = 7 ** 350 + 7 ** 150 - x
    s7 = ''
    while s > 0:
        s7 = str(s % 7) + s7
        s //= 7
    if s7.count('0') == 200:
        print(x)
        break