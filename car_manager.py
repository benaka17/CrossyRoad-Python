from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.allCars = []


    def createCar(self):
        randChance = random.randint(1,6)
        if randChance == 1:
            newCar = Turtle("square")
            newCar.shapesize(stretch_wid=1, stretch_len=2)
            newCar.penup()
            newCar.color(random.choice(COLORS))
            randY = random.randint(-250, 250)
            newCar.goto(300, randY)
            newCar.setheading(180)
            self.allCars.append(newCar)

    def moveCars(self):
        for car in self.allCars:
            car.forward(STARTING_MOVE_DISTANCE)