for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (((z <= x) and (x <= y)) or (w == (z or x))) == 0:
                    print(x, y, z, w)