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

john.speed(0)

for _ in range(90):
    john.color(random_color())
    john.circle(100)
    john.right(7)

screen.exitonclick()
