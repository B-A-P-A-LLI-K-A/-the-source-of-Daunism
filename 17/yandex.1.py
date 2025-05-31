sp = [int(i) for i in open('yandex.1')]
m = 0
spp = []
for i in sp:
    if m < i and len(str(i)) == 5 and str(i)[-2:] == '17':
        m = i
for i in range(len(sp) - 2):
    if sum([str(sp[i + r])[-2:] == '17' for r in range(3)]) > 0:
        if sum([abs(sp[i + r]) for r in range(3)]) <= m:
            spp.append(sum([sp[i + r] for r in range(3)]))
print(len(spp), min(spp))