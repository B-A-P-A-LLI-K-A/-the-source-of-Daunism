f = open('24_18284.txt').readline()
spl = []
spo = []
spv = []
spe = []
for i in range(len(f)):
    if f[i] == 'L':
        spl.append(i)
    if f[i] == 'O':
        spo.append(i)
    if f[i] == 'V':
        spv.append(i)
    if f[i] == 'E':
        spe.append(i)
print(min(spl), max(spl), min(spo), max(spo), min(spv), max(spv), min(spe), max(spe))
r = 0
k = 3000013
while r == 0:
    if f[k] == 'E':
        print(k)
        r = 1
    print(k)
    k += 1
print(k - 1, f[k - 1], 3000028 - 999998 + 1)
