from turtle import *
tracer(0)
screensize(5000, 5000)
k = 30

rt(30)
for _ in range(18):
    fd(11 * k)
    rt(120)
    fd(11 * k)
    rt(60)
up()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * k, y * k)
        dot(3, 'red')
done()