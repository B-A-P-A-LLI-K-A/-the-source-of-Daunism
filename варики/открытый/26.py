sp = [int(i) for i in open('26')]
sp.sort(reverse=True)
spk = []
for i in range(len(sp)):
    spp = [sp[i]]
    for y in range(i + 1, len(sp)):
        if sp[i] - sp[y] >= 9:
            spp.append(sp[y])
            i = y
    spk.append([len(spp), min(spp)])
spk.sort(key=lambda x: x[1])
spk.sort(reverse=True, key=lambda x: x[0])
print(spk[0])