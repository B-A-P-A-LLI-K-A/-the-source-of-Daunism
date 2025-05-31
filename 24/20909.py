f = open('20909').readline().strip()
sp = [i for i in range(len(f) - 1) if f[i] + f[i + 1] == 'AB']
print(max([sp[i + 101] - sp[i] for i in range(len(sp) - 101)]))