import turtle
from turtle import Turtle, Screen
import random


john = Turtle()
screen = Screen()
john.shape('turtle')
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        john.color(random_color())
        john.circle(100)
        john.setheading(john.heading() + size_of_gap)

john.speed(0)
draw_spirograph(7)

screen.exitonclick()
