import time
from turtle import Screen
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
    time.sleep(0.1)
    snake.move()

    if snake.snake[0].distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    if snake.snake[0].xcor() < -280 or snake.snake[0].xcor() > 280 or snake.snake[0].ycor() < -280 or snake.snake[0].ycor() > 280:
        scoreboard.reset()
        snake.reset()

    for body in snake.snake[1:]:
        if snake.snake[0].distance(body) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
