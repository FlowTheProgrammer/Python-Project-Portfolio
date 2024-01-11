from turtle import Turtle



class Paddle():
    def __init__(self):
        self.paddle = Turtle()
        self.createPaddle()

    def createPaddle(self):
            self.paddle.speed('fastest')
            self.paddle.color('green')
            self.paddle.shape('square')
            self.paddle.penup()
            self.paddle.shapesize(stretch_wid=7, stretch_len=1) 

    def moveUP(self):
      self.paddle.goto(self.paddle.xcor(),self.paddle.ycor() + 30)

    def moveDown(self):
        self.paddle.goto(self.paddle.xcor(),self.paddle.ycor() - 30)    