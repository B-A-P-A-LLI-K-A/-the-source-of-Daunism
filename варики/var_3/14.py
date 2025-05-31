sx = []
for x in range(1, 5556):
    s = 5 ** 150 + 5 ** 135 - x
    s5 = ''
    while s > 0:
        s5 = str(s % 5) + s5
        s //= 5
    if s5.count('4') == 134:
        sx.append(x)
print(max(sx))
