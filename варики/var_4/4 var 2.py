for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                F = (((a or b) <= ((1 - c) and a)) and d)
                if F == 1:
                    print(a, b, c, d)
