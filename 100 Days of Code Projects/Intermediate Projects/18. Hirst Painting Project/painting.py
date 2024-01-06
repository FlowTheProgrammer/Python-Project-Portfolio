import turtle
import colorgram
import random

"""
To get color list 

my_colors = []
colors = colorgram.extract('100 Days of Code Projects\Intermediate Projects/18. Hirst Painting Project\painting.jpg', 30)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    this_color = (r,g,b)
    my_colors.append(this_color)

print(my_colors)
"""
turtle.colormode(255)
lil_timmy = turtle.Turtle()
lil_timmy.speed(0)
lil_timmy.hideturtle()
color_list = [(202, 164, 110),  (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), 
(197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), 
(36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

for i in range(10):
    for j in range(10):
        lil_timmy.dot(20,random.choice(color_list))
        lil_timmy.penup()
        if j != 9:
            lil_timmy.forward(50)
        lil_timmy.pendown()
    if lil_timmy.heading() == 0:
        lil_timmy.penup()
        lil_timmy.left(90)
        lil_timmy.forward(50)
        lil_timmy.left(90)
        lil_timmy.pendown()
    elif lil_timmy.heading() == 180:
        lil_timmy.penup()
        lil_timmy.right(90)
        lil_timmy.forward(50)
        lil_timmy.right(90)
        lil_timmy.pendown()

