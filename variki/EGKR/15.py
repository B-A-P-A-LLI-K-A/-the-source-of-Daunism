for A in range(0, 500):
    f = 1
    for y in range(1, 500):
        for x in range(1, 500):
            if (((x - 3 * y) < A) or (y > 400) or (x > 56)) == 0:
                f = 0
    if f == 1:
        print(A)
