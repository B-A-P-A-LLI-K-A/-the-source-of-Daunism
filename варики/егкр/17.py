def m(a):
    if len(str(abs(a))) == 5:
        if str(a)[-2:] == '43':
            return 1


f = open('17')
sp = []
spm = []
sps = []
for i in f:
    sp.append(int(i.strip()))
    if m(int(i.strip())):
        spm.append(int(i.strip()))
d = max(spm)
for i in range(len(sp) - 2):
    if [m(sp[i + o]) for o in range(3)].count(1) > 0:
        if sum([sp[i + o] ** 2 for o in range(3)]) <= d ** 2:
            sps.append(sum([sp[i + o] ** 2 for o in range(3)]))
print(len(sps), min(sps))