import turtle


def draw(coordinates, color, turtle):
    turtle.fillcolor(color)

    turtle.up()
    turtle.goto(coordinates[3][0], coordinates[3][1])
    turtle.down()

    turtle.begin_fill()
    for i in range(len(coordinates)):
        print(i)
        turtle.goto((coordinates[i][0], coordinates[i][1]))
    turtle.end_fill()


def rect(c1, c2, type=0):
    if type == 0:
        return (abs(c1[0]) + abs(c2[0])) - (abs(c1[1]) + abs(c2[1])) // 3, c1[0]


# def mid(c1, c2):
#     return (c1[0] + c2[0]) / 2, (c1[1] + c2[1]) / 2


def test(coordinates):
    print(rect(coordinates[3], coordinates[0]))
    print(rect(coordinates[1], coordinates[2]))
    print(rect(coordinates[2], coordinates[3]))


def sierpinski(coordinates, level, colors, turtle):
    draw(coordinates, colors[level], turtle)

    if level > 0:
        sierpinski(
            [
                coordinates[0],
                rect(coordinates[3], coordinates[0]),
                rect(coordinates[1], coordinates[2]),
                rect(coordinates[2], coordinates[3])
            ],
            level - 1,
            colors,
            turtle
        )
        # sierpinski([coordinates[0],
        #             getMid(coordinates[0], coordinates[1]),
        #             getMid(coordinates[0], coordinates[2])],
        #            level - 1, turtle)
        # sierpinski([points[1],
        #             getMid(coordinates[0], coordinates[1]),
        #             getMid(coordinates[1], coordinates[2])],
        #            level - 1, turtle)
        # sierpinski([points[2],
        #             getMid(coordinates[2], coordinates[1]),
        #             getMid(coordinates[0], coordinates[2])],
        #            level - 1, turtle)


test([[-100, -150], [-200, 250], [300, 350], [400, -450]])
# pen = turtle.Turtle()
# pen.speed(1)
#
# win = turtle.Screen()
# sierpinski([[-250, -250], [-250, 250], [250, 250], [250, -250]], 1, ['blue', 'red'], turtle)
# print(rect([-250, -250], [250, -250], 0))
# draw([[-250, -250], [-250, 250], [250, 250], [250, -250]], 'blue', pen)
#
# pen.hideturtle()
# win.exitonclick()
