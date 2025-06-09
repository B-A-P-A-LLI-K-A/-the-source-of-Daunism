sp = [list(map(int, i.split())) for i in open('9')]
k = 0
for i in sp:
    o = [i.count(y) for y in i]
    o.sort()
    if o == [1, 1, 1, 1, 2, 2]:
        so = 0
        sp = 0
        for u in i:
            if u >= 0:
                sp += u
            else:
                so -= u
        if so > sp:
            k += 1
print(k)