k = 1
p = 0
for q in 'елопрст':
    for w in 'елопрст':
        for e in 'елопрст':
            for r in 'елопрст':
                for t in 'елопрст':
                    ch = q+w+e+r+t
                    if t == 'е' or t == 'о':
                        if k % 2 == 1:
                            if (5 - ch.count('е') - ch.count('о')) <= 3:
                                p += 1
                    k += 1
print(p)
