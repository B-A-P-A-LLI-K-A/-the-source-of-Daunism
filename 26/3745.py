sp = [[0 for _ in range(100)] for _ in range(100)]
spp = []
for i in open('3745'):
    i = list(map(int, i.split()))
    sp[i[0]][i[1]] = 1
for x in range(1, 98):
    for y in range(1, 98):
        if sp[x][y] == 1 and sp[x][y+1] == 1 and sp[x+1][y+1] == 1 and sp[x+1][y] == 1:
            if sp[x-1][y] == 0 and sp[x-1][y+1] == 0 and sp[x][y+2] == 0 and sp[x+1][y+2] == 0 and sp[x+2][y+1] == 0 and sp[x+2][y] == 0 and sp[x+1][y-1] == 0 and sp[x][y-1] == 0:
                spp.append([x, y])
spl = [0 for _ in range(105)]
for i in spp:
    spl[i[0]] += 1
    spl[i[0] + 1] += 1
print(len(spp), spl.index(max(spl)))