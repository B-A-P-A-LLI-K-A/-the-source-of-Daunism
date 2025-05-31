sp = [int(i) for i in open('17')]
m = 10 ** 10
spp = []
for i in sp:
    if i > 0 and str(i)[-2:] == '17' and i < m:
        m = i
for i in range(len(sp) - 2):
    if sum([sp[i + o] % m == 0 for o in range(3)]) == 1:
        if len(str(abs(sum([sp[i + o] for o in range(3)])))) == 4:
            spp.append(sum([sp[i + o] for o in range(3)]) ** 2)
print(len(spp), min(spp))