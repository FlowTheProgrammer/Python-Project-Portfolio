from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open('100 Days of Code Projects\Intermediate Projects/21. Snake Game\highscore.txt') as file:
            self.high_score = int(file.read())
            file.close
        self.shape('turtle')
        self.color('white')
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.score = 0
        self.goto(0,350)
        self.write(f"Score: {self.score}    High Score: {self.high_score}", align= 'center', font=('comic-sans',16),)

    def increaseByOne(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}    High Score: {self.high_score}", align= 'center', font=('comic-sans',16),)

    def newGame(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            self.writeToHighScore()
        self.score = 0 
        self.clear()
        self.write(f"Score: {self.score}    High Score: {self.high_score}", align= 'center', font=('comic-sans',16),)

    def writeToHighScore(self):
         with open('100 Days of Code Projects\Intermediate Projects/21. Snake Game\highscore.txt',mode='w') as file:
            file.write(str(self.score))
            file.close
         with open('100 Days of Code Projects\Intermediate Projects/21. Snake Game\highscore.txt') as file:
            self.high_score = int(file.read())
            file.close