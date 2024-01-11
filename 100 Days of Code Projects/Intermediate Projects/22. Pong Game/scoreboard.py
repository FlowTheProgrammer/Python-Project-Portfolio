from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.shape('turtle')
        self.color('white')
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.score1 = 0
        self.score2 = 0
        self.goto(0,350)
        self.write(f"{self.score2}     {self.score1}", align= 'center', font=('comic-sans',32),)

    def increaseByOnePlayer1(self):
        self.score1 += 1
        self.clear()
        self.write(f"{self.score2}     {self.score1}", align= 'center', font=('comic-sans',32),)

    def increaseByOnePlayer2(self):
        self.score2 += 1
        self.clear()
        self.write(f"{self.score2}     {self.score1}", align= 'center', font=('comic-sans',32),)