def r(a):
    s = 0
    for i in range(1, int(a ** 0.5) + 1):
        if a % i == 0:
            if i != a ** 0.5:
                s += (i + a / i)
            else:
                s += i
    return int(s)


k = 0
for n in range(500001, 1000000):
    if str(r(n))[-1] == '6':
        print(n, r(n))
        k += 1
    if k == 5:
        break