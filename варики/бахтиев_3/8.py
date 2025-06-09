from itertools import product
k = 1
kol = 0
for i in product('ЕЛОПРСТ', repeat=5):
    a = ''.join(i)
    if sum([a.count('ЕЛОПРСТ'[y]) for y in [1, 3, 4, 5, 6]]) <= 3:
        if a[-1] in 'ЕО' and k % 2 == 1:
            kol += 1
    k += 1
print(kol)