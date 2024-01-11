from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.shape('turtle')
        self.color('white')
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.score = 0
        self.goto(0,350)
        self.write(f"Score: {self.score}", align= 'center', font=('comic-sans',16),)

    def increaseByOne(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align= 'center', font=('comic-sans',16),)

    def gameOver(self):
        self.goto(0,0)
        self.write("GAME OVER!", align= 'center', font=('comic-sans',25),)