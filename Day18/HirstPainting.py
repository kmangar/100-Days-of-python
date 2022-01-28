# import colorgram
#
# colors = colorgram.extract('image.jpg', 30)
#
# color_tuple = []
#
# for x in range(30):
#     r = colors[x].rgb.r
#     g = colors[x].rgb.g
#     b = colors[x].rgb.b
#     color_tuple.append((r, g, b))
import turtle
from turtle import Turtle, Screen
import random


john = Turtle()
screen = Screen()
turtle.colormode(255)

colors = [(228, 157, 83), (41, 98, 159), (126, 174, 214), (244, 73, 32), (103, 197, 170), (239, 246, 252), (217, 74, 99), (30, 132, 53), (218, 180, 26), (166, 53, 81), (163, 73, 35), (44, 54, 143), (35, 62, 48), (213, 115, 151), (110, 47, 55), (71, 47, 56), (226, 208, 93), (78, 115, 191), (50, 184, 168), (5, 113, 54), (34, 37, 72), (155, 212, 194), (241, 170, 155), (230, 168, 180), (171, 186, 222), (156, 205, 215), (62, 153, 173)]

turtle.setpos(0, 0)

# for _ in range(100):
turtle.fillcolor(colors[0])
turtle.circle(20)

screen.exitonclick()