from turtle import Turtle
from random import randint

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.shapesize()
        self.color('green')
        self.speed(1)
        self.goto(0,0)
        self.ball_speed_y = 25
        self.ball_speed_x = 25
        
    def start(self):
        
        self.goto(self.xcor() + self.ball_speed_x , self.ycor() + self.ball_speed_y)

    def bounce(self):
        self.ball_speed_y *= -1

    def paddle_bounce(self):
        self.ball_speed_x *= -1