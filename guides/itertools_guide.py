from itertools import *
for i in product('1234', repeat = 3):   # 1) варианты ; 2) количество позиций
    print(i)

for i in permutations('1234'):  # меняет местами
    print(i)
