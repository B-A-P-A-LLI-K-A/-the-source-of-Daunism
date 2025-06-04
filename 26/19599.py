from math import ceil as c
sp = [list(map(int, i.split())) for i in open('19599')]
sp.sort(key=lambda x: x[0])
spgl = [0 for _ in range(len(sp) + 1)]
for i in sp:
    spgl[i[0]] = i[1]
for i in sp:
    if spgl[i[0]] != 0:
        if spgl[i[2]] != 0:
            spgl[i[2]] += spgl[i[0]]
        for h in range(3, 6):
            if spgl[i[0]] != 0:
                if spgl[i[h]] != 0:
                    if spgl[i[0]] > spgl[i[h]]:
                        spgl[i[0]] = c(spgl[i[0]] - spgl[i[0]] / 3)
                        spgl[i[h]] = 0
                    elif spgl[i[0]] < spgl[i[h]]:
                        spgl[i[h]] = c(spgl[i[h]] - spgl[i[h]] / 3)
                        spgl[i[0]] = 0
                    else:
                        spgl[i[0]] = 0
                        spgl[i[h]] = 0
print(spgl)
print(spgl.count(0) - 1, max(spgl))