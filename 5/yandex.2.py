def f(a):
    p = ''
    while a > 0:
        p = str(a % 3) + p
        a //= 3
    return p


sp = []
for n in range(1, 10000):
    q = f(n)
    s = ''
    for i in q:
        if i == '0':
            s += '1'
        if i == '1':
            s += '2'
        if i == '2':
            s += '0'
    k = 0
    s = str(int(s))
    l = ''
    for i in s:
        l = i + l
    l = l + f(sum([int(i) for i in l]))
    r = int(l, 3)
    if r > 10 ** 4:
        sp.append(r)
print(min(sp))