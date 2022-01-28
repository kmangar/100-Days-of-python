from turtle import Turtle, Screen
import random

john = Turtle()
screen = Screen()
# screen.exitonclick()
john.shape('turtle')
colors = ["slate gray", "medium violet red" ,"light blue", "silver", "cornflower blue", "pale violet red", "sandy brown", "dark violet", "light cyan"]

def draw_shape(num_of_sides):
    for _ in range(num_of_sides):
        angle = 360/num_of_sides
        john.forward(100)
        john.right(angle)

# print(random.choice(colors))

for x in range(3, 15):
    color = random.choice(colors)
    john.color(color)
    draw_shape(x)

screen.exitonclick()

print("HELLO")