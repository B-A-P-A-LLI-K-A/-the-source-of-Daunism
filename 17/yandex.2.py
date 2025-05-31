sp = [int(i) for i in open('yandex.2')]
spp = []
m = 10 ** 10
for i in sp:
    if len(str(abs(i))) == 3 and str(i)[-1] == '8':
        m = min(m, i)
for i in range(len(sp) - 2):
    if sum([sp[i + u] ** 2 > m ** 2 for u in range(3)]) == 2:
        if sum([len(str(abs(sp[i + u]))) == 3 for u in range(3)]) > 0:
            spp.append(sum([sp[i + u] for u in range(3)]))
print(len(spp), max(spp))