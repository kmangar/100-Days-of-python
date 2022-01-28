# import colorgram
# colors = colorgram.extract('image.jpg', 30)
#
# color_tuple = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_tuple.append((r, g, b))

import turtle
from turtle import Turtle, Screen
import random


john = Turtle()

turtle.colormode(255)

colors = [(228, 157, 83), (41, 98, 159), (126, 174, 214), (244, 73, 32), (103, 197, 170), (239, 246, 252), (217, 74, 99), (30, 132, 53), (218, 180, 26), (166, 53, 81), (163, 73, 35), (44, 54, 143), (35, 62, 48), (213, 115, 151), (110, 47, 55), (71, 47, 56), (226, 208, 93), (78, 115, 191), (50, 184, 168), (5, 113, 54), (34, 37, 72), (155, 212, 194), (241, 170, 155), (230, 168, 180), (171, 186, 222), (156, 205, 215), (62, 153, 173)]
john.penup()
john.hideturtle()
ypos = -300
john.setpos(-300, ypos)


def one_row():
    for _ in range(10):
        john.dot(20, random.choice(colors))
        john.penup()
        john.forward(50)

john.speed(0)
for x in range(10):
     one_row()
     ypos += 50
     john.setpos(-300, ypos)

screen = Screen()
screen.exitonclick()