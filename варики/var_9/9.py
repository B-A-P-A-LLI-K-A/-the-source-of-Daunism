sp = [list(map(int, i.split())) for i in open('9')]
k = 0
for i in sp:
    if sum([len(str(i[p])) == 3 for p in range(6)]) >= 3:
        if sum([i[p] % 5 == 0 for p in range(6)]) == 0:
            k += 1
print(k)