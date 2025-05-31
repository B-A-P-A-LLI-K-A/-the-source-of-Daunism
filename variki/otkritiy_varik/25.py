def r(a):
    s = 0
    for i in range(1, int(a ** 0.5) + 1):
        if a % i == 0:
            if a ** 0.5 == i:
                s += i
            else:
                s += i
                s += a // i
    return s


k = 0
for n in range(500001, 600000):
    if str(r(n))[-1] == '6':
        print(n, r(n))
        k += 1
    if k == 5:
        break