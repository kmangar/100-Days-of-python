import turtle as t

screen = t.Screen()
bud = t.Turtle()


def move_fd():
    bud.forward(10)


def move_b():
    bud.backward(10)


def move_right():
    bud.rt(10)


def move_left():
    bud.lt(10)

def clear_screen():
    bud.clear()
    bud.penup()
    bud.home()
    bud.pendown()


screen.listen()
screen.onkey(key="c", fun=clear_screen)
screen.onkey(key="w", fun=move_fd)
screen.onkey(key="s", fun=move_b)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)


screen.exitonclick()




