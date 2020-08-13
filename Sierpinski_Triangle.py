# Name:             Joel Tan
# Admin No:         174866J
# Tutorial Group:   IT1204-04

import turtle as t


# expects 2D array for coordinates [[left x, left y], [top x, top y], [right x, right y]]
def draw(coordinates, color, turtle):
    turtle.fillcolor(color)
    turtle.up()
    turtle.goto(coordinates[0][0], coordinates[0][1])
    turtle.down()
    turtle.begin_fill()
    turtle.goto(coordinates[1][0], coordinates[1][1])
    turtle.goto(coordinates[2][0], coordinates[2][1])
    turtle.goto(coordinates[0][0], coordinates[0][1])
    turtle.end_fill()


def mid(c1, c2):
    return (c1[0] + c2[0]) / 2, (c1[1] + c2[1]) / 2


# expects 2D array for coordinates [[left x, left y], [top x, top y], [right x, right y]]
def sierpinski(coordinates, level, colors, turtle):
    draw(coordinates, colors[level], turtle)

    if level > 0:
        sierpinski(
            [
                coordinates[0],
                mid(coordinates[0], coordinates[1]),
                mid(coordinates[0], coordinates[2])
            ],
            level - 1,
            colors,
            turtle
        )

        sierpinski(
            [
                coordinates[1],
                mid(coordinates[0], coordinates[1]),
                mid(coordinates[1], coordinates[2])
            ],
            level - 1,
            colors,
            turtle
        )

        sierpinski(
            [
                coordinates[2],
                mid(coordinates[2], coordinates[1]),
                mid(coordinates[0], coordinates[2])
            ],
            level - 1,
            colors,
            turtle
        )


# Main
win = t.Screen()
pen = t.Turtle()
pen.speed(1)

sierpinski(
    [[-200, -50], [0, 200], [200, -50]],
    5,
    ['blue', 'red', 'green', 'cyan', 'yellow', 'pink'],
    pen
)

pen.hideturtle()
win.exitonclick()
