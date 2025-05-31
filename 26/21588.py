s = 74619
sp = [list(map(int, i.split(' '))) for i in open('21588')]
sp.sort()
print(sp)
p = 1
for i in sp:
    