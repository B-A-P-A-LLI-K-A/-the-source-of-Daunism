for A in range(100):
    fl = 1
    for x in range(100):
        for y in range(100):
            f = (5 < y) or (x > 32) or ((x + 2 * y) < A)
            if f == 0:
                fl = 0
    if fl == 1:
        print(A)
        break