sp = [list(map(int, i.split())) for i in open('9')]
k = 0
for i in sp:
    i.sort()
    if 2 * (sum(i[-2:])) > 3 * (sum(i) - sum(i[-2:])):
        if sum([str(i[p])[-1] == '5' for p in range(5)]) >= 2:
            k += 1
print(k)