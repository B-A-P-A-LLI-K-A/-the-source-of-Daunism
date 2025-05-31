def f(a):
    su = 0
    for i in a:
        su += int(i)
    return su


sn = []
for n in range(10, 10000):
    n2 = bin(n)[2:]
    if f(n2) % 2 == 0:
        n2 = '10' + n2[2:] + '0'
    else:
        n2 = '11' + n2[2:] + '1'
    r = int(n2, 2)
    if r > 171:
        sn.append(n)
print(min(sn))
