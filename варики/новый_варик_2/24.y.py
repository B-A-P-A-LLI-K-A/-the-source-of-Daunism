f = open('24.x').readline().strip().split('QQ')
sp = [len(i) for i in f]
print(max([sum(sp[i:i + 102]) + 2 * 100 - 2 for i in range(len(sp) - 102)]))