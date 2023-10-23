import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STARTING_CARS = 5

class CarManager():

    # 2. Cars are randomly generated along the y-axis and will move from the right edge of the screen to the left edge.

    def __init__(self):
        self.all_car = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.amount_of_cars = STARTING_CARS

    def speed_up(self):
        self.car_speed += MOVE_INCREMENT

    def add_cars(self):
        self.amount_of_cars += 1

    def new_car(self):
        # chance = random.randint(1, 6)

        check = random.randint(1, 6)
        for car in self.all_car:
            if car.xcor() < -300:
                car.goto(300, random.randrange(-245, 245))
        if check == 1 and len(self.all_car) < self.amount_of_cars:
            next_car = Turtle()
            next_car.penup()
            next_car.color(random.choice(COLORS))
            next_car.shape("square")
            next_car.shapesize(stretch_len=2, stretch_wid=1)
            next_car.setheading(180)
            next_car.goto(300, random.randrange(-245, 245))
            self.all_car.append(next_car)

    def car_move(self):
        for car in self.all_car:
            car.forward(self.car_speed)

