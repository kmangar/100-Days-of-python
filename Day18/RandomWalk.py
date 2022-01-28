import turtle
from turtle import Turtle, Screen
import random

john = Turtle()
screen = Screen()
john.shape('turtle')
turtle.colormode(255)

directions = [0, 90, 180, 270]


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def random_walk():
    color = random_color()
    john.color(color)
    compass = random.choice(directions)
    john.forward(30)
    john.setheading(compass)


john.pensize(12)
john.speed(0)

for _ in range(500):
    random_walk()

screen.exitonclick()
