from turtle import *
tracer(0)
screensize(5000, 5000)
k = 30

for _ in range(13):
    fd(13 * k)
    rt(90)
    fd(5 * k)
up()
rt(90)
fd(7 * k)
lt(90)
fd(10 * k)
down()
for _ in range(23):
    fd(8 * k)
    lt(90)
    fd(11 * k)
    lt(90)
up()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * k, y * k)
        dot(3, 'red')
done()