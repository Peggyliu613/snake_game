import time
from turtle import Turtle, Screen
import snake
import food
import scoreboard


screen = Screen()
screen.setup(600, 600)
screen.bgcolor("pink")
screen.title("Snake Game")
screen.tracer(0)

snake = snake.Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


food = food.Food()
scoreboard = scoreboard.Scoreboard()


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.3)
    snake.move()

    if snake.snake[0].distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    if snake.snake[0].xcor() < -280 or snake.snake[0].xcor() > 280:
        game_is_on = False
    if snake.snake[0].ycor() < -280 or snake.snake[0].ycor() > 280:
        game_is_on = False

    for body in snake.snake:
        if body != snake.snake[0]:
            if snake.snake[0].distance(body) < 10:
                game_is_on = False

scoreboard.game_over()

screen.exitonclick()
