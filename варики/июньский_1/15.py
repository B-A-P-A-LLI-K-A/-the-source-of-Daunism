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


for t in range(1000):
    fl = 0
    for x in range(1000):
        r = ((f(x, 117) != 0) and (f(x, 91) == 0)) <= (not(f(x, t) == 0))
        if r == 0:
            fl = 1
            break
    if fl == 0:
        print(t)
        break