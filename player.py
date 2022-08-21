from turtle import Turtle

STARTING_POSITION = (0, -250)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def up(self):
        self.forward(MOVE_DISTANCE)

    def down(self):
        self.back(MOVE_DISTANCE)

    def left(self):
        self.goto(self.xcor()-10, self.ycor())

    def right(self):
        self.goto(self.xcor()+10, self.ycor())

    def finish(self):
        self.goto(STARTING_POSITION)
