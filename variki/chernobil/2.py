for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = not(w) and z and (x <= y)
                if f == 1:
                    print(x, y, z, w)