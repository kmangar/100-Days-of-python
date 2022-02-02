from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 16, "bold")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        with open("highscore.txt") as file:
            self.high_score = int(float(file.read()))

        self.penup()
        self.color("white")
        self.goto(-5, 275)
        self.score_update()

    def score_update(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def reset(self):

        if self.score > self.high_score:
            self.high_score = self.score
            with open("highscore.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.score_update()

    def keeper(self):
        self.score += 1
        self.score_update()
