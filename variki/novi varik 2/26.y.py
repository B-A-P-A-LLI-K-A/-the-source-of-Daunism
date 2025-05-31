f = open('26.x')
l = 0
o = []
n, m, k = list(map(int, f.readline().split(' ')))
sp = [m] * (k + 1)
for i in range(n):
    r, me = list(map(int, f.readline().strip().split(' ')))
    sp[me] = min(sp[me], r - 1)
for i in range(len(sp) - 1):
    o.append([min(sp[i], sp[i + 1]), i])
print(max(o, key=lambda x: x[1]))