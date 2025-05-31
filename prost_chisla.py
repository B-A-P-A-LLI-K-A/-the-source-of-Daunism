import time
sp = [2]
x = int(input())
t1 = time.time()
for per in range(3, x + 1):
    flag = 0
    last = 1
    for rez in range(last - 1, len(sp)):
        if sp[rez] > (int(per ** 0.5) + 1):
            last = rez
            break
    for prost in sp[0: last]:
        if per % prost == 0:
            flag = 1
            break
    if flag == 0:
        sp.append(per)
print(sp)
t2 = time.time()
print(t2 - t1)
