'''import sys
sys.setrecursionlimit(10000)
def f(n):
    if n <= 3:
        return n - 1
    elif n % 2 == 0:
        return f(n - 2) + n / 2 - f(n - 4)
    else:
        return f(n - 1) * n + f(n - 2)


print(f(4952) + 2 * f(4958) + f(4964))
'''
sp = [-1, 0, 1, 2]
for _ in range(5000):
    sp.append(0)
for n in range(4, 5000):
    if n % 2 == 0:
        sp[n] = sp[n - 2] + n / 2 - sp[n - 4]
    else:
        sp[n] = sp[n - 1] * n + sp[n - 2]
print(sp[4952] + 2 * sp[4958] + sp[4964])