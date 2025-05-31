f = open('9.x')
sp = []
k = 0
for i in f:
    sp.append(list(map(int, i.strip().split('	'))))
for i in sp:
    if 2 * max(i) < sum(i):
        if len(set(i)) == 3:
            k += 1
print(k)