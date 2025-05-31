def f(a):
    s = ''
    while a > 0:
        s = str(a % 3) + s
        a //= 3
    return s


for n in range(1, 1000):
    t = f(n)
    r = ''
    if n % 3 == 0:
        for i in t:
            r += i
            r += i
    else:
        for i in t:
            if i == '0':
                r += '1'
                r += '1'
            if i == '1':
                r += '2'
                r += '2'
            if i == '2':
                r += '0'
                r += '0'
    u = int(r, 3)
    if u > 120:
        print(n)
        break
