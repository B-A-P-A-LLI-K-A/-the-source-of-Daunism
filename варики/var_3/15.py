def d(a, b):
    if a % b == 0:
        return 1
    else:
        return 0


for A in range(1, 200):
    f = 0
    for x in range(1, 200):
        l = (not(d(x, 7)) and d(x, 13)) <= (x > A - 40)
        if l == 0:
            f = 1
    if f == 0:
        print(A)
