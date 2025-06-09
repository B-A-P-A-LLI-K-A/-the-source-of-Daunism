def f(c, b):
    if c % b == 0:
        return 1
    else:
        return 0


for a in range(1000, 0, -1):
    fl = 0
    for x in range(1, 1000):
        t = (((not(f(x, 7))) and f(x, 13)) <= (x > (a - 40)))
        if t == 0:
            fl = 1
            break
    if fl == 0:
        print(a)
        break