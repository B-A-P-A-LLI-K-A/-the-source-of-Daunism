for n in range(7, 100):
    s = '0' * 19 + '1' * n + '2' * 19
    s = ''.join(s)
    s = '>' + s
    while '>1' in s or '>2' in s or '>0' in s:
        if '>1' in s:
            s = s.replace('>1', '22>', 1)
        if '>2' in s:
            s = s.replace('>2', '2>', 1)
        if '>0' in s:
            s = s.replace('>0', '1>', 1)
    if int(str(sum([int(i) for i in s if i != '>']))[-2:]) % 11 == 0:
        print(n)
        break