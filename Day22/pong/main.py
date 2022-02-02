from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.title("PONG")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(left_paddle.up, "w")
screen.onkeypress(left_paddle.down, "s")

screen.onkeypress(right_paddle.up, "Up")
screen.onkeypress(right_paddle.down, "Down")

game_is_on = True

while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    # DETECT Collision with top and bottom wall
    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce_y()

    # DETECT collision with paddle
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or (ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # DETECT right ball out of bounds
    if ball.xcor() > 380:
        ball.reset_postion()
        scoreboard.left_point()

    # DETECT left ball out of bounds
    if ball.xcor() < -380:
        ball.reset_postion()
        scoreboard.right_point()

    if scoreboard.left_score == 11:
        ball.stop()
        winner_name = screen.textinput(title="WE have a WINNER!!", prompt="You are the Winner!! What's your Name: ")
        print(f"The winner is {winner_name}")
        exit(1)

    if scoreboard.right_score == 11:
        ball.stop()
        winner_name = screen.textinput(title="WE have a WINNER!!", prompt="You are the Winner!! What's your Name: ")
        print(f"The winner is {winner_name}")
        exit(1)



screen.exitonclick()
