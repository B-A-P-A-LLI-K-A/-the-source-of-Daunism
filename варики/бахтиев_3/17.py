sp = [int(i) for i in open('17')]
m = 10 ** 10
k = []
for i in sp:
    if i > 0 and i % 10 == 4:
        m = min(i, m)
for i in range(len(sp) - 2):
    if sum([sum([int(r) for r in str(abs(sp[i + p]))]) for p in range(3)]) == m:
        k.append(sum([sp[i + p] for p in range(3)]))
print(len(k), max(k))