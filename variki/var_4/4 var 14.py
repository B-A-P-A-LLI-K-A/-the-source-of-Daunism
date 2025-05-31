def f(a, sis):  # Функция перевода числа из системы счисления < 37, в 10-ричную
    it = 0
    k = len(a) - 1
    for i in a:
        it += int(i, sis) * (sis ** k)
        k -= 1
    return it


pr = 1
for p in range(30, 37):
    for s in range(10, 35):
        if f('R4', p - 1) + f('B0', s + 2) + f('T3NK4', p) == 23593399:
            pr = pr * p * s
print(pr)
