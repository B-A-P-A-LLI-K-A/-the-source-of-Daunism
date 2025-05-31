def c(a):
    if len(str(abs(a))) == 5:
        return 1
    else:
        return 0


kol = 0
m = 10 ** 10
spp = []
f = open('17_18368.txt')
sp = []
for i in f:
    sp.append(int(i))
    if abs(int(i)) % 10 == 7:
        if int(i) < m:
            m = int(i)

for i in range(len(sp) - 2):
    if c(sp[i]) or c(sp[i + 1]) or c(sp[i + 2]):
        if sp[i] * sp[i + 1] * sp[i + 2] % m == 0:
            kol += 1
            spp.append(sp[i] * sp[i + 1] * sp[i + 2])
print(kol, max(spp), m)
