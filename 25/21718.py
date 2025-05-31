import re
for n in range(7993, 10 ** 10 + 1, 7993):
    if re.fullmatch('4[0123456789]*4736[0123456789]*1', str(n)):
        print(n, n // 7993)