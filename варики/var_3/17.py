def sc(a):
    s = 0
    a = str(abs(a))
    for p in a:
        s += int(p)
    return s


f = open('17_18176.txt')
kol = 0
spp = []
sp = []
ms = []
for i in range(1112):
    u = int(f.readline())
    sp.append(u)
    if u % 10 == 4 and u > 0:
        ms.append(u)
m = min(ms)

for i in range(len(sp) - 2):
    if sc(sp[i]) + sc(sp[i + 1]) + sc(sp[i + 2]) == m:
        kol += 1
        spp.append(sp[i] + sp[i + 1] + sp[i + 2])
print(kol, max(spp))
