for s in range(2):
    for r in range(2):
        for a in range(2):
            for t in range(2):
                if ((s or (not(r))) and (not(r == a)) and t):
                    print(s, r, a, t)