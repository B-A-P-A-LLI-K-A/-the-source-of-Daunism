spr = []
for n in range(1, 1000):
    r = oct(n)[2:]
    if n % 2 == 0:
        for i in r:
            if int(i) % 2 != 0:
                r = r.replace(i, '2', 1)
    else:
        r = '3' + r[1:-1] + '3'
    r = int(r, 8)
    if r < 300:
        spr.append(r)
print(max(spr))