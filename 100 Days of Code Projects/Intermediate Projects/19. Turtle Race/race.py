from turtle import Turtle, Screen
import random

#Screen Setup
screen = Screen()
screen.setup(width=500,height=400)
the_bet  = screen.textinput(title = 'Who will win?', prompt = "Enter the name of the race you wish to win!")

#Lists
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
racers = []

#Variables
pos = -150
still_racing = True

for i in range(7):
    racer = Turtle()
    racer.shape('turtle')
    racer.color(colors[i])
    racer.penup()
    racer.goto(-230,pos)
    pos += 50
    racers.append(racer)

while still_racing:
    for racer in racers: 
        racer.forward(random.randint(0,10))
        if racer.xcor() > 220:
            still_racing = False
            winner = racer.color()[1]

if the_bet.lower() == winner.lower():
    print(f'{winner.capitalize()} won! Your bet was right!')
else:
    print(f'{winner.capitalize()} won! Your bet was wrong, try again!')
    




screen.exitonclick()