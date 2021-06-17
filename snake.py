from turtle import Turtle


class Snake:

    def __init__(self):
        self.snake = []
        for i in range(3):
            self.snake.append(Turtle(shape="square"))
            self.snake[i].color("white")
            self.snake[i].penup()
            self.snake[i].goto(x=i * -20, y=0)

    def add_part(self, position):
        self.snake.append(Turtle(shape="square"))
        self.snake[-1].color("white")
        self.snake[-1].penup()
        self.snake[-1].goto(position)

    def reset(self):
        for seg in self.snake:
            seg.goto(1000,1000)
        self.snake.clear()
        self.__init__()

    def extend(self):
        self.add_part(self.snake[-1].position())

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

    def left(self):
        if self.snake[0].heading() != 0:
            self.snake[0].setheading(180)

    def right(self):
        if self.snake[0].heading() != 180:
            self.snake[0].setheading(0)

