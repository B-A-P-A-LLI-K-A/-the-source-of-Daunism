import re
s = '1'
x = 0
for f in range(1, 40):
    s += ('|' + str(2 ** f))
s = '8902\d{2}' + '(' + s + ')'
for i in range(1432, 10 ** 10 + 1, 1432):
    if x < 5:
        if re.fullmatch(s, str(i)):
            print(i, i // 1432)
            x += 1