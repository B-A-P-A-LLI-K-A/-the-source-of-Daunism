for n in range(4, 10000):
    s = '5' + '7' * n
    while '57' in s or '477' in s or '7777' in s:
        if '57' in s:
            s = s.replace('57', '7', 1)
        if '477' in s:
            s = s.replace('477', '75', 1)
        if '7777' in s:
            s = s.replace('7777', '4', 1)
    if sum([int(i) for i in s]) == 36:
        print(n)
        break