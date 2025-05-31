for q in range(2):
    for p in range(2):
        for a in range(2):
            f = (p <= ((q and (not(a))) <= (not(p))))
            if f == 0:
                print(p, q, a)