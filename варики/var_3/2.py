for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                F = ((a <= b) == c) or d
                if F == 0:
                    print(a, b, c, d)
