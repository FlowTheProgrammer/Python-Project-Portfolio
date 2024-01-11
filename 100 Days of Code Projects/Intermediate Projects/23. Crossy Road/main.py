from turtle import Screen
from scoreboard import Scoreboard
from player import Player
from car import Cars
from random import randint
import time

#Screen Setup
myScreen = Screen()
myScreen.setup(width=600, height=600)
myScreen.title("Crossy Road")
myScreen.tracer(0)
myScreen.bgcolor("gray")

player = Player()
scoreboard = Scoreboard()
cars= Cars()


myScreen.onkeypress(player.moveUP, "space")
#myScreen.onkeypress(player1.moveDown, "Down")

game_on = True

myScreen.listen()


while game_on:
    myScreen.update()
    time.sleep(.1)
    cars.createCar()
    cars.moveForward()
    if player.ycor() > 270:
        player.nextLevel()
        scoreboard.increaseByOne()
        cars.nextLevel()
    for car in cars.cars:
        car_y= car.ycor()
        y = abs(car.ycor() - player.ycor())
        abs_x = abs(car.xcor())
        if (y < 25 and abs_x <=  20):
            game_on = False
            scoreboard.gameOver()
        if car.xcor() > 400:
            cars.cars.remove(car)

myScreen.exitonclick()      
         