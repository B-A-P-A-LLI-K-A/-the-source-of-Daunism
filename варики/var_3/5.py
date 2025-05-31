spr = []
for n in range(1, 10000):
    n3 = ''
    s = 0
    while n > 0:
        n3 = str(n % 3) + n3
        s += n % 3
        n //= 3
    if s % 2 == 0:
        n3 = '1' + n3 + '2'
    else:
        n3 = '2' + n3 + '0'
    if int(n3, 3) > 100:
        spr.append(int(n3, 3))
print(min(spr))
