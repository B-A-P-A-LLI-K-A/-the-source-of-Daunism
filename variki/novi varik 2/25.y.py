def f(a):
    for i in range(2, int(a // 2) + 1):
        if a % i == 0:
            return i + a // i
    return 0


print(f(12))
for u in range(700000, 700050):
    if f(u) % 10 == 4:
        print(u, f(u))