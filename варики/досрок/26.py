a = open('26')
f = int(a.readline())
sp = [int(a.readline()) for i in range(f)]
sp.sort()
spi = []
spp = []
x = 0
for i in sp:
    if i >= (x + 9):
        x = i
        spp.append(x)
k = len(spp)
for i in range(len(sp)):
    x = sp[i]
    spp = [x]
    for u in range(i + 1, len(sp)):
        if sp[u] >= (x + 9):
            x = sp[u]
            spp.append(x)
    if len(spp) == k:
        spi.append(sp[i])
print(k, max(spi))