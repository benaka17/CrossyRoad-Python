from turtle import Turtle

FONT = ("Courier", 12, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-250, 250)
        self.updateScore()

    def increaseLevel(self):
        self.level += 1
        self.updateScore()

    def updateScore(self):
        self.clear()
        self.write(f"Level: {self.level}", False, "center", FONT)


