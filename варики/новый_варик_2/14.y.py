for x in range(1, 2031):
    n = 3 ** 100 - x
    s = ''
    while n > 0:
        s = str(n % 3) + s
        n //= 3
    if s.count('0') == 1:
        print(x)