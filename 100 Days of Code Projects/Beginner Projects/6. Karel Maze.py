"""
Basic Karel Maze
Loops/Functions

https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

Link to Karel Maze

"""

#Loop to get the robot out of any position in the maze
def turn_right():
    turn_left()
    turn_left()
    turn_left()
while not at_goal():
    
    if right_is_clear():
        turn_right()
        move()
    elif not right_is_clear():
        turn_left()