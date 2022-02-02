from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.scoreUpdate()

    def scoreUpdate(self):
        self.clear()
        self.goto(-290, 260)
        self.write(f"LEVEL: {self.level}", align="left", font=FONT)

    def levelUp(self):
        self.level += 1
        self.scoreUpdate()
