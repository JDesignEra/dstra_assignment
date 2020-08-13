# Name:             Joel Tan
# Admin No:         174866J
# Tutorial Group:   IT1204-04

import turtle as t
import math


def draw(radius, color, turtle):
    # turtle.up()
    # turtle.right(180)
    # turtle.down()

    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()


def sierpinski(radius, level, colors, turtle):
    draw(radius, colors[level], turtle)

    if level > 0:
        #turtle.up()
        #turtle.forward(radius / 4)
        #turtle.right(90)
        #turtle.forward(radius / 4)
        #turtle.down()
        # sierpinski(radius / 2.5, level - 1, colors, turtle)


        #turtle.up()
        #turtle.goto((turtle.xcor() + radius) * 2 / 4.5, (turtle.ycor() + radius) * 2 / 4.5)
        #turtle.down()
        #sierpinski(radius / 2.5, level - 1, colors, turtle)

        turtle.up()
        turtle.goto(turtle.xcor() - math.ceil(radius / (1 + math.sqrt(2))), turtle.ycor() + radius)
        turtle.down()
        sierpinski(radius / (1 + math.sqrt(2)), level - 1, colors, turtle)

        turtle.up()
        turtle.goto(turtle.xcor() + 2 * math.floor(radius / (1 + math.sqrt(2))), turtle.ycor())
        turtle.down()
        sierpinski(radius / (1 + math.sqrt(2)), level - 1, colors, turtle)

        turtle.up()
        turtle.goto(turtle.xcor(), turtle.ycor() - 2 * math.floor(radius / (1 + math.sqrt(2))))
        turtle.down()
        sierpinski(radius / (1 + math.sqrt(2)), level - 1, colors, turtle)


win = t.Screen()
pen = t.Turtle()
pen.speed(10)

radius = 200

# Center initial drawing
# pen.up()
# pen.goto(0, radius * -1)
# pen.down()

# draw(radius, 'blue', pen)
sierpinski(
    radius,
    2,
    ['blue', 'red', 'green', 'cyan', 'yellow', 'pink'],
    pen
)

pen.hideturtle()
win.exitonclick()