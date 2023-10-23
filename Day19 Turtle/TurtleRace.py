import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False

user_bet = screen.textinput(title="Make your bet", prompt="Which Turtle will win the race? Enter a color: ")
colors = ["red", "blue", "green", "purple", "orange", "khaki"]
coordinates = [150, 100, 50, 0, -50, -100]
racers = []

for index_range in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[index_range])
    new_turtle.penup()
    new_turtle.goto(-230, coordinates[index_range])
    racers.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in racers:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won!! The {winning_color} turtle is the winner!!")
            else:
                print(f"You've lost! The {winning_color} turtle is not the winner!")
        rand_pace = random.randint(0, 10)
        turtle.forward(rand_pace)


screen.exitonclick()





