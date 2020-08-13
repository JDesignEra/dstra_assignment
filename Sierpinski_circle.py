# Name:             Joel Tan
# Admin No:         174866J
# Tutorial Group:   IT1204-04

import turtle as t
import math


def draw(radius, color, turtle):
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()


def sierpinski(radius, level, colors, turtle):
    draw(radius, colors[level], turtle)

    if level > 0:
        turtle.up()
        turtle.left(90)
        turtle.forward(radius - radius / (1 + math.sqrt(2)))
        turtle.right(180)
        turtle.down()
        sierpinski(radius / (1 + math.sqrt(2)), level - 1, colors, turtle)

        turtle.up()
        turtle.backward(2 * radius / (1 + math.sqrt(2)))
        turtle.down()
        sierpinski(radius / (1 + math.sqrt(2)), level - 1, colors, turtle)

        turtle.up()
        turtle.right(90)
        turtle.forward(2 * radius / (1 + math.sqrt(2)))
        turtle.left(90)
        turtle.down()
        sierpinski(radius / (1 + math.sqrt(2)), level - 1, colors, turtle)

        turtle.up()
        turtle.forward(radius + radius / (1 + math.sqrt(2)))
        turtle.left(90)
        turtle.forward(2 * radius / (1 + math.sqrt(2)))


win = t.Screen()
pen = t.Turtle()
pen.speed(50)

radius = 500

# Center initial drawing
pen.up()
pen.goto(0, -radius)
pen.down()

sierpinski(
    radius,
    5,
    ['blue', 'red', 'green', 'cyan', 'yellow', 'pink'],
    pen
)

pen.hideturtle()
win.exitonclick()
