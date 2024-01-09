from turtle import Turtle



class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(5, 1)
        self.speed("fastest")
        self.penup()
        self.goto(position)
        self.color("white")




    def moveUp(self):
        new_y = self.ycor() + 25
        self.goto(self.xcor(), new_y)

    def moveDown(self):
        new_y = self.ycor() -25
        self.goto(self.xcor(), new_y)



