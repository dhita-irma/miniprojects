import turtle


def draw_triangle(points, color, t):
    """
    Draw a triangle located in the 3 points
    :param points: 3 points of the triangle (a list of 3 coordinates (x, y))
    :param color: the color to fill the triangle
    :param t: turtle object
    """
    t.fillcolor(color)                    # Fill color, take 'color' parameter
    t.up()                                # Lift pen up
    t.goto(points[0][0], points[0][1])    # Go to the first point of triangle (bottom left)
    t.down()                              # Put pen down
    t.begin_fill()                        # Begin to fill the shape that's about to be drawn
    t.goto(points[1][0], points[1][1])    # Go to the second point of triangle (upper middle) while drawing a line
    t.goto(points[2][0], points[2][1])    # Go to the third point of triangle (bottom right) while drawing a line
    t.goto(points[0][0], points[0][1])    # Go back to the first point (bottom left) while drawing a line
    t.end_fill()                          # Finish filling color


def get_mid(p1, p2):
    """Return coordinate (x, y) between p1 and p2"""
    return (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2


def sierpinski(points, degree, t):
    colormap = ['blue', 'red', 'green', 'violet', 'yellow', 'white', 'orange']
    draw_triangle(points, colormap[degree], t)
    if degree > 0:
        sierpinski([points[0],
                    get_mid(points[0], points[1]),
                    get_mid(points[0], points[2])],
                   degree - 1, t)
        sierpinski([points[1],
                    get_mid(points[0], points[1]),
                    get_mid(points[1], points[2])],
                   degree - 1, t)
        sierpinski([points[2],
                    get_mid(points[2], points[1]),
                    get_mid(points[0], points[2])],
                   degree - 1, t)


if __name__ == '__main__':

    my_turtle = turtle.Turtle()
    my_win = turtle.Screen()
    my_turtle.speed(1)

    # x and y coordinates for 3 points of triangle
    my_points = [[-100, -50], [0, 100], [100, -50]]

    sierpinski(my_points, 3, my_turtle)
    my_win.exitonclick()
