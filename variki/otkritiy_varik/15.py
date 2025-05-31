def f(a, b):
    a = bin(a)[2:]
    b = bin(b)[2:]
    if len(a) < len(b):
        q = a
        a = b
        b = q
    while len(a) > len(b):
        b = '0' + b
    q = ''
    for i in range(len(a)):
        q += str(int(a[i]) * int(b[i]))
    return int(q, 2)


for w in range(1000):
    r = 0
    for x in range(1000):
        g = (((f(x, 52) != 0) and (f(x, 48) == 0)) <= (not(f(x, w) == 0)))
        if g == 0:
            r = 1
            break
    if r == 0:
        print(w)
        break