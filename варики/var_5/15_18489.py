def c(q, w):
    if q % 10 == w % 10:
        return 1
    else:
        return 0


for a in range(1, 500):
    f = 0
    for x in range(1, 500):
        if ((not c(x, 5) and c(x, 4)) <= (x > (a - 11))) == 0:
            f = 1
    if f == 0:
        print(a)
