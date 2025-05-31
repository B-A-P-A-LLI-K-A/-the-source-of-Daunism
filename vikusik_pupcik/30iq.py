sp = []
for n in range(4, 1234):
    n2 = bin(n)[2:]
    if n % 2 == 0:
        n2 = n2 + n2[-3:]
    else:
        n2 = '1'+ n2 + '01'
    r = int(n2, 2)
    if r > 600:
        sp.append(r)
print(min(sp))
