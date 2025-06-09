def q(a):
    d = set()
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            d.add(i)
            d.add(a // i)
    return sorted(d)


k = 0
for i in range(9500000, 10000000):
    f = [x for x in q(i) if len(q(x)) == 0]
    if len(f) != 0:
        f = sum(f) // len(f)
        if f % 813 == 0:
            print(i, f)
            k += 1
        if k == 5:
            break