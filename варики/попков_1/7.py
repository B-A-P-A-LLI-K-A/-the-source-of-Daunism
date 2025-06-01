from itertools import product
k = 0
for i in product('ВЬЮГА', repeat=6):
    if 'ЮГ' in ''.join(i):
        k += 1
print(k)