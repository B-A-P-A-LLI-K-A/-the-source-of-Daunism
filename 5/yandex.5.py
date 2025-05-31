def f(a):
    s = ''
    while a > 0:
        s = str(a % 3) + s
        a //= 3
    return s


spn = []
spr = []
for n in range(1, 10000):
    q = f(n) + f(n)[-1]
    if sum([int(i) for i in f(n)]) % 3 == 0:
        q = '2' + q + '1'
    else:
        q = q + f((sum([int(i) for i in f(n)]) % 3) * 2)
    r = int(q, 3)
    if r > 1000:
        spr.append(r)
        spn.append(n)
print(spn[spr.index(min(spr))])