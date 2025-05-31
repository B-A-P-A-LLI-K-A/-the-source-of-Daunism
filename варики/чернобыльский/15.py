for a in range(1, 100):
    f = 0
    for x in range(1, 1000000):
        if (((x % a == 0) and (x % 845 == 0)) <= (x % 325 == 0)) == 0:
            f = 1
    if f == 0:
        print(a)
        break