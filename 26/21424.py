f = open('21424')
n = int(f.readline().strip())
sp = []
for i in f:
    sp.append(int(i.strip()))
sp.sort()
x = sp[0]
sps = []
for i in range(0, len(sp)):
    if x <= (sp[i] - 9):
        sps.append(sp[i])
        x = sp[i]
for i in range(len(sp)):
    x = sp[i]
    spk = []
    for u in range(i, len(sp)):
        if x <= (sp[u] - 9):
            spk.append(sp[u])
            x = sp[u]
    if len(spk) == len(sps):
        print(sp[i])
print(len(sps) + 1)