'''def poisk(spis, sim):
    it = []
    for q in range(len(spis)):
        if spis[q] == sim:
            it.append(q)
    return it


def oper(spis, op, zn):
    w = 0
    if zn == '*':
        for q in op:
            spis.insert(q - w, spis[q - w] * spis[q + 1 - w])
            spis.pop(q + 1 - w)
            spis.pop(q + 1 - w)
            w += 1
    if zn == '+':
        for q in op:
            spis.insert(q - w, spis[q - w] + spis[q + 1 - w])
            spis.pop(q + 1 - w)
            spis.pop(q + 1 - w)
            w += 1
    if zn == '/':
        for q in op:
            spis.insert(q - w, spis[q - w] / spis[q + 1 - w])
            spis.pop(q + 1 - w)
            spis.pop(q + 1 - w)
            w += 1
    if zn == '-':
        for q in op:
            spis.insert(q - w, spis[q - w] - spis[15+25q + 1 - w])
            spis.pop(q + 1 - w)
            spis.pop(q + 1 - w)
            w += 1
    if zn == '**':
        for q in op:
            spis.insert(q - w, spis[q - w] ** spis[q + 1 - w])
            spis.pop(q + 1 - w)
            spis.pop(q + 1 - w)
            w += 1
    return spis, w


g = input()
spot = [-1]
spza = []
m = 0
spc = []
var = ['**', '*', '/', '+', '-']

for v in range(len(g)):
    d = v - m
    if g[d] == '(':
        spot.append(d)
    if g[d] == ')':
        spza.append(d)
    if g[d] == ' ':
        g = g[:d] + g[d + 1:]
        m += 1
        print('Пиши без пробелов дура, но я и так посчитаю')
spot = spot[::-1]
spza.append(len(g))
b = 0
z = 0
fl = 0
for za in spza:
    for ot in spot:
        if za > ot:
            spc = []
            spz = []
            ch = ''
            a = g[(ot + 1):za - z + b]
            z = len(a) + 2
            for c in range(len(a)):
                i = a[c]
                if i in '0123456789':
                    ch += i
                    if c == len(a) - 1:
                        spc.append(int(ch))
                elif ch != '' and i != '*':
                    spc.append(int(ch))
                    spz.append(i)
                    ch = ''
                elif i == '*' and a[c + 1] == '*':
                    spc.append('**')
                    fl = 1
                elif i == '-':
                    ch += i
                elif fl == 0:
                    spc.append(i)
                else:
                    fl = 0
            for u in var:
                sp = oper(spc, poisk(spz, u), u)
                spc = sp[0]
                for l in range(sp[1]):
                    spz.remove(u)
            spc = str(spc[0])
            b = len(spc)
            print(g[:ot],'     ', g[(za + 1):])
            g = g[:ot] + spc + g[(za + 1):]
            spot.remove(ot)
            print(g, a, z, b, spc, spz)
            break
print(spc)
'''