import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():

    # 2. Cars are randomly generated along the y-axis and will move from the right edge of the screen to the left edge.

    def __init__(self):
        self.all_car = []

    def new_car(self):
        chance = random.randint(1, 6)

        if chance == 1:

            new_car = Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.speed(5)
            new_car.goto(300, random.randint(-245, 245))
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.setheading(180)
            # self.car_move()
            self.all_car.append(new_car)

    def car_move(self):

        for car in self.all_car:
                car.forward(STARTING_MOVE_DISTANCE)
