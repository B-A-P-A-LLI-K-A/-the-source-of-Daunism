for a in range(2):
    for p in range(2):
        for q in range(2):
            for r in range(2):
                if ((q <= p) or ((not(a)) <= r)) == 0:
                    print(a, p, q, r)