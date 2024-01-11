from turtle import Turtle
import random
from random import randint

speed = 10


class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
        self.cars = []
        self.speed = speed
        self.hideturtle()

    def createCar(self):
        chance = randint(1,5)
        if chance == 1:
            car = Turtle()
            car.setheading(180)
            car.color(random.choice(self.colors))
            car.shape("square")
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.penup()
            car.goto(300,random.randint(-250,250))
            self.cars.append(car)

    def moveForward(self):
        for car in self.cars:
            car.forward(self.speed)

    def nextLevel(self):
        self.speed += 10