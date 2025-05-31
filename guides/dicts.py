r = {'123' : 1234, '234' : 23345}
print(r, type(r), r['123'])
r['123'] = 123456
print(r['123'])
s = ['a', 'b']
p = [1, 2]
sp = dict(zip(s, p))
print(sp)
