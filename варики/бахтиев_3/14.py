for x in range(5555, 0, -1):
    s = 5 ** 150 + 5 ** 135 - x
    k = ''
    while s > 0:
        k = str(s % 5) + k
        s //= 5
    if k.count('4') == 134:
        print(x)
        break