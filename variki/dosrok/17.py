sp = [int(i) for i in open('17')]
s = 0
k = 0
spp = []
for i in sp:
    if i < 0:
        s += i
for i in range(len(sp) - 2):
    if (max([sp[u] for u in range(i, i + 3)]) * min([sp[u] for u in range(i, i + 3)])) > s:
        k += 1
        spp.append(sum([sp[u] for u in range(i, i + 3)]))
print(k, abs(max(spp)))