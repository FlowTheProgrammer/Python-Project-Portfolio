from turtle import Screen
import time
from snake import Snake

#Screen Setup
myScreen = Screen()
myScreen.setup(width=800, height=800)
myScreen.title("Snake Game")
myScreen.tracer(0)
myScreen.bgcolor("black")
    

game_snake = Snake()

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
    

myScreen.exitonclick()      