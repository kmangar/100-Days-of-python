from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 16, "bold")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(-5, 275)
        self.score_update()

    def score_update(self):
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)
    
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!!", False, align=ALIGNMENT, font=FONT)

    
    def keeper(self):
        self.score += 1
        self.clear()
        self.score_update()
