import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
scoreboard = Scoreboard()
car = CarManager()

screen.listen()

screen.onkey(turtle.up, "Up")
screen.onkey(turtle.down, "Down")
screen.onkey(turtle.left, "Left")
screen.onkey(turtle.right, "Right")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.createCar()
    car.moveCars()

    if turtle.ycor() == 280:
        turtle.finish()
        scoreboard.increaseLevel()

    for cars in car.allCars:
        if turtle.distance(cars) < 15:
            game_is_on = False
            turtle.hideturtle()
            turtle.goto(0,0)
            turtle.write("GAME OVER", False, "center", ("Arial", 24, "normal"))

    screen.update()

screen.exitonclick()