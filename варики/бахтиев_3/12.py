sp = []
for n in range(4, 10000):
    s = '4' + '1' * n
    while '411' in s or '1111' in s:
        if '411' in s:
            s = s.replace('411', '14', 1)
        if '1111' in s:
            s = s.replace('1111', '1', 1)
    sp.append(sum([int(i) for i in s]))
print(max(sp))