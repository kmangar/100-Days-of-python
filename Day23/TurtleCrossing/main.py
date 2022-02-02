import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move, "w")
screen.onkey(player.move, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # When the turtle hits the top edge of the screen,
    # it moves back to the original position and the player levels up. On the next level, the car speed increases.
    if player.ycor() == 280:
        player.respawn()

    car_manager.new_car()
    car_manager.car_move()
