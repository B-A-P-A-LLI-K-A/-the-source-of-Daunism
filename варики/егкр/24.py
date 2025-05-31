f = open('24').readline().strip()
sp = []
for i in range(len(f) - 3):
    if f[i] +  f[i + 1] + f[i + 2] + f[i + 3] == 'FSRQ':
        sp.append(i)
spl = [sp[80] + 2]
for i in range(len(sp) - 81):
    spl.append(sp[i + 81] - sp[i] + 2)
print(max(spl))