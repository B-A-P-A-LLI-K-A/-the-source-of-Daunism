for n in range(1, 1000):
    r = bin(n)[2:]
    if sum([int(i) for i in r]) % 2 == 0:
        r = '11' + (r + '1')[2:]
    else:
        if r.count('0') < r.count('1'):
            r += '0'
        else:
            r += '1'
    r = int(r, 2)
    if r > 271:
        print(n)
        break