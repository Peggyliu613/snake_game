import time
from turtle import Screen
from snake import Snake

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("pink")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.5)
    snake.move()


screen.exitonclick()
