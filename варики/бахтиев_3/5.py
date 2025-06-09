spr = []
for n in range(1, 10000):
    k = n
    s = ''
    while k > 0:
        s = str(k % 3) + s
        k //= 3
    if sum([int(i) for i in s]) % 2 == 0:
        s = '1' + s + '2'
    else:
        s = '2' + s + '0'
    r = int(s, 3)
    print(n, r)
    if r > 100:
        spr.append(r)
print(min(spr))