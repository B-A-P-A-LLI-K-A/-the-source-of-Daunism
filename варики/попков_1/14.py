for x in range(2024, -1, -1):
    s = 9 ** 2024 + 9 ** 1987 - x
    d = ''
    while s > 0:
        d = str(s % 9) + d
        s //= 9
    if d.count('8') == 1984:
        print(x)
        break