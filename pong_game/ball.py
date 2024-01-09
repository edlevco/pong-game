from turtle import Turtle

class Ball(Turtle):


    def __init__(self, position):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(position)
        self.y_move = 5
        self.x_move = 5
        self.move
        self.bounce

    
    def move(self):
        x_pos = self.xcor() + self.x_move
        y_pos = self.ycor() + self.y_move
        self.goto(x_pos, y_pos)

    def bounce(self, surface):
        if surface == "wall":
            self.y_move *= -1
        else:
            self.x_move *= -1

