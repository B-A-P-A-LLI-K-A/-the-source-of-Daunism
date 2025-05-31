spr = []
for n in range(1, 100000):
    n2 = bin(n)[2:]
    if len(n2) % 2 == 0:
        n2 = n2 + '1'
    else:
        n2 = '1' + n2 + '0'
    r = int(n2, 2)
    if r > 666:
        spr.append(r)
print(min(spr))
