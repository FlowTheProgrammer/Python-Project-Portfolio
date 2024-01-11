from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

#Screen Setup
myScreen = Screen()
myScreen.setup(width=1200, height=800)
myScreen.title("Pong")
myScreen.tracer(0)
myScreen.bgcolor("black")

player1 = Paddle()
player2 = Paddle()
ball = Ball()

player1.paddle.goto(550,0)
player2.paddle.goto(-550,0)
    
scoreboard = Scoreboard()
myScreen.onkeypress(player1.moveUP, "Up")
myScreen.onkeypress(player1.moveDown, "Down")
myScreen.onkeypress(player2.moveUP, "w")
myScreen.onkeypress(player2.moveDown, "s")

game_on = True

myScreen.listen()

while game_on:
    myScreen.update()
    time.sleep(.1)
    ball.start()

    if ball.ycor() > 370 or ball.ycor() < -370:
        ball.bounce()
        
    if (ball.distance(player1.paddle) < 50 and ball.xcor() > 520) or (ball.distance(player2.paddle) < 50 and ball.xcor() < -520):
        ball.paddle_bounce()

    if ball.xcor() > 580 or ball.xcor() < -580:
        if ball.xcor() > 580:
            scoreboard.increaseByOnePlayer2()
        else:
             scoreboard.increaseByOnePlayer1()
        ball.goto(0,0)
    

myScreen.exitonclick()      