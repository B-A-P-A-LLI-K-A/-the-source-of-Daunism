sp = [list(map(int, i.strip().split(' '))) for i in open('14253')]
k = 0
for i in sp:
    spp = [i.count(u) for u in i]
    spp.sort()
    if spp == [1, 2, 2, 2, 2, 2, 2] or (sum(i) / 7) ** 0.5 == int((sum(i) / 7) ** 0.5):
        k += 1
print(k)