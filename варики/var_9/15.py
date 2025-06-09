for a in range(1, 1000):
    fl = 0
    for x in range(1, 1000):
        if ((a + 2 * x > 400 - a) and ((a % 100 + 120 % a) > 140)) == 0:
            fl = 1
            break
    if fl == 0:
        print(a)
        break