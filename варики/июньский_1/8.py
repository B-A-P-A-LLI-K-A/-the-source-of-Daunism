from itertools import product
k = 0
for i in product('АБЕИЛРТФЦ', repeat=5):
    r = ''.join(i)
    if r[-1] in 'АЕЛТЦ':
        if r[0] in 'БЛРТФЦ':
            if r.count('Ц') == r.count('Ф'):
                k += 1
print(k)