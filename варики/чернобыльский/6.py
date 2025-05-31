from turtle import *
tracer(0)
screensize(5000, 5000)
r = 50
for _ in range(12):
    fd(5 * r)
    rt(150)
    fd(5 * r)
    lt(105)
up()
rt(90)
fd(3 * r)
rt(90)
fd(2 * r)
down()
for _ in range(17):
    fd(6 * r)
    rt(90)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * r, y * r)
        dot(3, 'red')
update()
done()