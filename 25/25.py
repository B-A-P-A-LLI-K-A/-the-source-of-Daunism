def f(a):
    for u in range(8, a // 2 + 1):
        if a % u == 0 and str(u)[-1] == '7' and a != u:
            return u
    return 0


k = 0
for i in range(1125001, 1250000):
    if k < 5:
        if f(i) != 0:
            print(i, f(i))
            k += 1
    else:
        break