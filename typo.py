import time
sp = []
x = int(input())
t1 = time.time()
for n in range(2, x + 1):
    f = 0
    for u in range(2, int(n ** 0.5) + 1):
        if n % u == 0:
            f = 1
    if f == 0:
        sp.append(n)
print(sp)
t2 = time.time()
print(t2 - t1)