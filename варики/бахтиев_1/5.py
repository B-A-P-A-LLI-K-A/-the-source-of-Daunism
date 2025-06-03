spr = []
for n in range(1, 10000):
    i = bin(n)[2:]
    if sum([int(o) for o in i]) % 2 == 0:
        i += '11'
    else:
        i += '01'
    print(n, int(i, 2))
    if int(i, 2) > 61:
        spr.append(int(i, 2))
print(min(spr))