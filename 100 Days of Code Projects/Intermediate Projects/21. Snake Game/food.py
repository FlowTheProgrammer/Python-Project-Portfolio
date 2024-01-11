from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.shapesize(stretch_len=.5, stretch_wid=.5)
        self.color('red')
        self.speed("fastest")
        self.goto(randint(-250,250),randint(-250,250))
        
    def eaten(self):
        self.goto(randint(-250,250),randint(-250,250))