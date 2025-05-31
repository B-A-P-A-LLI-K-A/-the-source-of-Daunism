f = [list(map(int, i.split(' '))) for i in open('9')]
k = 0
for i in f:
    s = set(i)
    if len(s) == len(i):
        i.sort()
        if sum(i[3:]) <= sum(i[:3]):
            k += 1
print(k)