def a(q):
    su = 1
    k = 1
    for u in range(2, int(q ** 0.5) + 1):
        if q % u == 0:
            if u == (q / u):
                su += u
                k += 1
            else:
                su += u
                su += (q / u)
                k += 2
    return int(su // k)


f = 0
for i in range(769999, 769500, -1):
    if a(i) % 100 == 12 and f < 5:
        print(i, a(i))
        f += 1