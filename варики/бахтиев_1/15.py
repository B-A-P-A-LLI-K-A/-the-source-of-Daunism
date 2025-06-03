for a in range(1000):
    fl = 0
    for x in range(1000):
        for y in range(1000):
            f = ((x <= 19) or (y < 2 * x + a - 50) or (y > 17))
            if f == 0:
                fl = 1
                break
        if fl == 1:
            break
    if fl == 0:
        print(a)
        break