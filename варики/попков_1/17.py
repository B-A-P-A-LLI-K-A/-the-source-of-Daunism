sp = [int(i) for i in open('17')]
k = 0
spp = []
for i in sp:
    if i % 2 == 0:
        k += 1
for i in range(len(sp) - 1):
    if sum([sp[i + p] > 0 for p in range(2)]) > 0:
        if sum([sp[i + p] for p in range(2)]) < k:
            spp.append(sum([sp[i + p] ** 2 for p in range(2)]))
print(len(spp), max(spp))