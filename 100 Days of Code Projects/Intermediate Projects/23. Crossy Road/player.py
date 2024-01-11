from turtle import Turtle



class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color('white','black')
        self.shapesize(stretch_len=1.15, stretch_wid=1.15)
        self.penup()
        self.setheading(90)
        self.goto(0,-270)
    
    def moveUP(self):
        self.forward(10)

    def nextLevel(self):
        self.goto(0,-270)