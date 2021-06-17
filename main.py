import time
from turtle import Screen

from scoreboard import Scoreboard
from food import Food
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.snake[0].distance(food) < 15:
        scoreboard.update_score()
        food.refresh()
        snake.extend()


    if snake.snake[0].xcor() > 290 or snake.snake[0].xcor() < -290 or snake.snake[0].ycor() > 290 or snake.snake[0].ycor() < -290:
        scoreboard.reset()
        snake.reset()

    for part in snake.snake[1:]:
        if snake.snake[0].distance(part) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
