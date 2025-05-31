from re import *
spo = []
for i in range(18579, 10 ** 10 + 1, 18579):
    if fullmatch(r'54[0123456789]1[0123456789]3[0123456789]*7', str(i)):
        spo.append([i, i // 18579])
for i in range(len(spo)):
    print(spo[i][0], spo[i][1])