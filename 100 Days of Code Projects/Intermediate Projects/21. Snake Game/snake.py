from turtle import Turtle



class Snake():
    def __init__(self):
        self.snake_body = []

        self.positions = [(0,0),(-20,0),(-40,0)]

        #Snake Body Creation
        for i in self.positions:
            self.createSegment(i)

    def createSegment(self, position):
            body_part = Turtle()
            body_part.speed('fastest')
            body_part.color('white', 'green')
            body_part.shape('square')
            body_part.penup()
            body_part.goto(position)
            self.snake_body.append(body_part)    

    def movement(self):
        for body in self.snake_body[::-1]:
            if self.snake_body.index(body) != 0:
                body.goto(self.snake_body[self.snake_body.index(body) - 1].pos())
                self.snake_body[self.snake_body.index(body) - 1].forward(20)

    def up(self):
        if self.snake_body[0].heading() != 270:
            self.snake_body[0].setheading(90)

    def down(self):
        if self.snake_body[0].heading() != 90:
            self.snake_body[0].setheading(270)

    def left(self):
        if self.snake_body[0].heading() != 0:
            self.snake_body[0].setheading(180)

    def right(self):
        if self.snake_body[0].heading() != 180:
            self.snake_body[0].setheading(0)

    def extendBody(self):
        self.createSegment(self.snake_body[-1].position())