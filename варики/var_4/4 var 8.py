k = 0
bibl = '0123456789AB'
for q in bibl:
    for w in bibl:
        for e in bibl:
            for r in bibl:
                for t in bibl:
                    for y in bibl:
                        ch = q + w + e + r + t + y
                        if q != '0':
                            if ch.count('B') == 1:
                                cet = 0
                                nec = 0
                                for i in ch:
                                    if i in '02468A':
                                        cet += 1
                                    else:
                                        nec += 1
                                if cet == nec:
                                    k += 1
print(k)
