def m(a):
    b = ''
    while a > 0:
        b = str(a % 3) + b
        a //= 3
    return b


spr = []
for n in range(1, 10000):
    n3 = m(n)
    if n % 3 == 0:
        n3 = n3 + n3[-2:]
    else:
        s = [int(i) for i in n3]
        n3 = n3 + m(sum(s))
    r = int(n3, 3)
    if r % 2 == 0 and r > 220:
        spr.append(r)
print(min(spr))