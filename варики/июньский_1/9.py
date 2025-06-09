from math import prod
sp = [list(map(int, i.split())) for i in open('9')]
k = 0
for i in sp:
    o = [i.count(u) for u in i]
    if o == [1, 1, 1, 1, 1, 1, 1]:
        i.sort()
        if prod(i[:2]) <= sum(i[2:]):
            k += 1
print(k)