for i in range(1, 10000):
    n = bin(i)[2:]
    n += str(sum([int(i) for i in n]) % 2)
    n += str(sum([int(i) for i in n]) % 2)
    if int(n, 2) > 253:
        print(i)
        break