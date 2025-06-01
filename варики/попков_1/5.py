spr = []
for n in range(1, 26):
    i = bin(n)[2:]
    if n % 2 == 0:
        i = '10' + i + '0111'
    else:
        i = '10' + i + '1'
    spr.append(int(i, 2))
print(max(spr))