sp = [list(map(int, i.split(' '))) for i in open('9')]
k = 0
for i in sp:
    c = [i.count(u) for u in i]
    s = c.copy()
    c.sort()
    if c == [1, 1, 1, 1, 2, 2, 2, 2]:
        if max([i[e] for e in range(8) if s[e] == 2]) < (sum([i[e] for e in range(8) if s[e] == 1]) / 4):
            k += 1
print(k)