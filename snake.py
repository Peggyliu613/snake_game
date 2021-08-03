from turtle import Turtle


class Snake:
    def __init__(self):
        self.snake = []

        location = 0
        for i in range(3):
            shu = Turtle("square")
            shu.color("white")
            shu.penup()
            shu.goto(location, 0)
            location -= 20
            self.snake.append(shu)

    def move(self):
        for i in range(len(self.snake) - 1, 0, -1):
            self.snake[i].goto(self.snake[i - 1].xcor(), self.snake[i - 1].ycor())
        self.snake[0].forward(20)

    def up(self):
        if self.snake[0].heading() != 270:
            self.snake[0].setheading(90)

    def down(self):
        if self.snake[0].heading() != 90:
            self.snake[0].setheading(270)

    def right(self):
        if self.snake[0].heading() != 180:
            self.snake[0].setheading(0)

    def left(self):
        if self.snake[0].heading() != 0:
            self.snake[0].setheading(180)
