sp = [list(map(int, i.split(' '))) for i in open('egkr')]
for i in range(len(sp)):
    print(sp[i][1])