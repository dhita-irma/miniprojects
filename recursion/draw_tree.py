import turtle


def tree(branch_len, width, t):
    if branch_len > 5:
        if branch_len <= 15:
            t.color("green")
        t.pensize(width)
        t.forward(branch_len)

        t.right(20)
        tree(branch_len - 15, width - 5, t)

        t.left(40)
        tree(branch_len - 15, width - 5, t)

        t.right(20)
        t.backward(branch_len)
        t.color("brown")                        # Reset the color back to brown


if __name__ == '__main__':
    t = turtle.Turtle()
    win = turtle.Screen()
    t.left(90)   # Turn turtle left by 90 degrees
    t.up()       # Lift pen up
    t.backward(100)   # Move to the opposite direction
    t.down()          # Put pen down
    t.color("brown")  # Set color to x
    tree(75, 25, t)
    win.exitonclick()
