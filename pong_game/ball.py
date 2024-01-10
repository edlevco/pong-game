from turtle import Turtle

class Ball(Turtle):


    def __init__(self, position):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(position)
        self.y_move = 20
        self.x_move = 20
        self.move_speed = 0.09


    
    def move(self):
        x_pos = self.xcor() + self.x_move
        y_pos = self.ycor() + self.y_move
        self.goto(x_pos, y_pos)

    def bounce(self, surface):
        if surface == "wall":
            self.y_move *= -1
        else:
            self.x_move *= -1
            self.move_speed *= 0.5
            print(self.move_speed)

    def resetPosition(self):
        self.move_speed = 0.09
        self.hideturtle()
        self.setpos(0, 0)
        self.showturtle()
        self.x_move *= -1

