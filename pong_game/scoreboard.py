from turtle import Turtle
ALIGN = "center"
FONT = ("arial", 80, "normal")





class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.left_score = 0
        self.right_score = 0
        self.updateScore()
        
    def updateScore(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_score, align=ALIGN, font=FONT)
        self.goto(100, 200)
        self.write(self.right_score, align=ALIGN, font=FONT)


    def point(self, point):
        if point == "left":
            self.left_score += 1
        else:
            self.right_score += 1
        self.updateScore()


        
        
        
