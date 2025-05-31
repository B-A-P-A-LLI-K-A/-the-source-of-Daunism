for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = ((z <= x) and (not(y) and (not(w) == y)))
                if f == 0 and y == 1 and w == 0:
                    print(x, y, z, w, f)