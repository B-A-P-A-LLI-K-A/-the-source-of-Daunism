from itertools import *

def f(x, y, z, w):
    return not((not(x) or y) and not(w)) or not(z and not(y and w))


for a1, a2, a3, a4, a5, a6, a7 in product([0, 1], repeat = 7):
    t = [(0, a1, a2, 1), (a3, 1, a4, a5), (1, 0, a6, a7)]
    k = 0
    if len(t) == len(set(t)):
        for i in permutations('xyzw'):
            k = 0
            for u in t:
                if f(**dict(zip(i, u))) == 0:
                    k += 1
            if k == 3:
                print(i)
