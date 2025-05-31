sp = [[1, 2, 3, 4, 5, 6], [4, 5, 4, 5, 4, 8], [6, 6, 6, 6, 6, 7]]
for i in sp:
    spp = []
    spq = []
    spw = []
    spd = []    #Для вида
    for x in i:
        spp.append(i.count(x))
    for x in range(len(spp)):
        if spp[x] != 1:
            spq.append(x)
    for x in spq:
        spw.append(i[x])
    spw = set(spw)
    if len(spw) != 0:
        for t in spw:
            spd.append(i.count(t))
            for p in range(i.count(t)):
                i.remove(t)
    print(i, '- Неповторяющтеся числа')
    print(spw, '- Повторяющтеся числа')
    print(spd, '- Количество повторяющися чисел')
'''
for i in f:
    sp.append(f.count(i))
for i in range(len(sp)):
    if sp[i] != 1:
        spp.append(i)
for i in spp:
    sppp.append(f[i])
sppp = set(sppp)
'''
