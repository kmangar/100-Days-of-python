from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.finishLine = FINISH_LINE_Y
        self.respawn()

    def respawn(self):
        self.penup()
        self.shape("turtle")
        self.goto(STARTING_POSITION)
        self.setheading(90)

    # 1. A turtle moves forwards when you press the "Up" key. It can only move forwards, not back, left or right.
    def move(self):
        if self.ycor() != FINISH_LINE_Y:
            self.forward(MOVE_DISTANCE)

