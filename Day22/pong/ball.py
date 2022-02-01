from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()

        # FOR BOUNCE
        self.x_new = 10
        self.y_new = 10

        # BALL speed
        self.ball_speed = 0.1


    def move(self):
        x = self.xcor() + self.x_new
        y = self.ycor() + self.y_new
        self.goto(x, y)

    def bounce_y(self):
        self.y_new *= -1

    def bounce_x(self):
        self.x_new *= -1
        self.ball_speed *= 0.9

    def reset_postion(self):
        self.goto(0, 0)
        self.ball_speed = 0.1
        self.bounce_x()

    def stop(self):
        self.x_new = 0
        self.y_new = 0