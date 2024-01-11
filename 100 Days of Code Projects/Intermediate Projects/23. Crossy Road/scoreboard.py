from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('white','black')
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.level = 1
        self.goto(-290,250)
        self.write(f"Level: {self.level}", font=('comic-sans',20))
    def increaseByOne(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", font=('comic-sans',20))

    def gameOver(self):
        self.goto(0,0)
        self.write("GAME OVER!", align= 'center', font=('comic-sans',25),)
