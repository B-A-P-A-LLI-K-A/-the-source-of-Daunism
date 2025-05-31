from guides.itertools_guide import *

k = 0
for i in product('АВИЙКПС', repeat = 6):
    s = ''.join(i)
    if 'АА' in s or'АИ' in s or 'ИА' in s or 'ИИ' in s:
        k += 1
    if s == 'КАКААА':
        print(k)

