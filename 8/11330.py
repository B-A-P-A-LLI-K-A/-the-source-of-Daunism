from itertools import product
a = 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'
a = sorted(a, reverse=True)
a.insert(26, 'Ё')
b = 'ИНФОРМАТИКА'
k = 1
for i in range(len(b)):
    k += a.index(b[i]) * len(a) ** (len(b) - 1 - i)
print(k)