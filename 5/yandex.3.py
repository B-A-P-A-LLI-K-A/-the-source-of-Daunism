def f(a):
    s = ''
    while a > 0:
        s = str(a % 3) + s
        a //= 3
    return s


spn = []
spr = []
for n in range(1, 10000):
    q = f(n)
    if sum([int(i) for i in q]) % 2 == 0:
        q = '2' + q[2:] + '0'
    else:
        q = '20' + q[2:] + '1'
    r = int(q, 3)
    if r > 75:
        spn.append(n)
        spr.append(r)
print(spn[spr.index(min(spr))])