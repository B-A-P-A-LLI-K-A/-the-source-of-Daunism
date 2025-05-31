spr = []
for n in range(1, 10000):
    q = bin(n)[2:]
    if n % 2 == 0:
        q = '1' + q + '00'
    else:
        q += bin(sum([int(i) for i in q]))[2:]
    r = int(q, 2)
    if r > 205:
        spr.append(r)
print(min(spr))