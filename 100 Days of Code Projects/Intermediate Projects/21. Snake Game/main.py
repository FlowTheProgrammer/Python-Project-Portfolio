from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

#Screen Setup
myScreen = Screen()
myScreen.setup(width=800, height=800)
myScreen.title("Snake Game")
myScreen.tracer(0)
myScreen.bgcolor("black")
    

game_snake = Snake()
chow_time =  Food()
scoreboard = Scoreboard()

head = game_snake.snake_body[0]

myScreen.listen()

myScreen.onkeypress(game_snake.up, "Up")
myScreen.onkeypress(game_snake.down, "Down")
myScreen.onkeypress(game_snake.left, "Left")
myScreen.onkeypress(game_snake.right, "Right")


#Game Logic
game_on = True
while game_on:
    myScreen.update()
    time.sleep(.1)
    game_snake.movement()

    if head.distance(chow_time) < 20:
        chow_time.eaten()
        scoreboard.increaseByOne()
        game_snake.extendBody()

    if head.xcor() > 395 or head.xcor() < -395:
        game_snake.reset()
        head = game_snake.snake_body[0]
        scoreboard.newGame()

    if head.ycor() > 395 or head.ycor() < -395:
        game_snake.reset()
        head = game_snake.snake_body[0]
        scoreboard.newGame()

    for segment in game_snake.snake_body[1:]:
        if head.distance(segment) < 15:
            game_snake.reset()
            head = game_snake.snake_body[0]
            scoreboard.newGame()
    

myScreen.exitonclick()      