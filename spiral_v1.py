from turtle import *
import colorsys
bgcolor("black")
setup(width=970, height=640)
pensize(3)
tracer (10)
h = 0

for x in range(190):
    c = colorsys.hsv_to_rgb(h,1,1)
    fillcolor(c)
    h += 0.0096

    begin_fill()
    up()
    forward(x)
    down ()
    right(9)
    forward(x)
    right(100)
    right(10)
    end_fill()

    for j in range(36):
        forward(x)
        right(83)
        backward(x)
deturtle()