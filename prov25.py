def m(a):
    o = 1
    sp = []
    for i in range(2, a // 2 + 1):
        o += 1
        if a % i == 0:
            sp.append(i)
        print(o)
    return sp


spp = [int(i) for i in open('prov25')]
ss = [m(i) for i in spp]
print(ss)