f = [int(i) for i in open('17')]
x = 10 ** 10
sp = []
for i in f:
    if i < x and len(str(abs(i))) == 3 and str(i)[-2:] == '15':
        x = i
for i in range(len(f) - 2):
    if sum([f[i + p] >= 0 for p in range(3)]) == 3 or sum([f[i + p] >= 0 for p in range(3)]) == 0:
        if max([f[i + p] for p in range(3)]) * min([f[i + p] for p in range(3)]) > x ** 2:
            sp.append(max([f[i + p] for p in range(3)]) * min([f[i + p] for p in range(3)]))
print(len(sp), min(sp))