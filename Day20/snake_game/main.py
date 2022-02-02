import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE GAME!")
screen.tracer(0)

game_is_on = True
snake = Snake()
food = Food()
score = Score()


screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")


while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # DETECT collision with food
    if snake.head.distance(food) < 15:
        score.keeper()
        food.refresh()
        snake.extend()
    # Detect collision with wall
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        snake.reset()
        score.reset()

    # DETECT collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            snake.reset()
            score.reset()
    # if head collides with any segment in the tail

screen.exitonclick()

