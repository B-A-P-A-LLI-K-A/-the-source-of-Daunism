def f(a):
    s = ''
    while a > 0:
        s = str(a % 3) + s
        a //= 3
    return s


spr = []
for n in range(1, 10000):
    q = f(n)
    if sum([int(i) for i in q]) % 2 == 0:
        q = '211' + (q + '20')[3:]
    else:
        q = '102' + (q + '01')[3:]
    r = int(q, 3)
    if r > 300:
        spr.append(r)
print(min(spr))