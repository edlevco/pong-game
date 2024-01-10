from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
ball = Ball((0, 0))
scoreboard = Scoreboard()



screen.listen()

screen.onkeypress(key="Up", fun = right_paddle.moveUp)
screen.onkeypress(key="Down", fun = right_paddle.moveDown)
screen.onkeypress(key="w", fun = left_paddle.moveUp)
screen.onkeypress(key="s", fun = left_paddle.moveDown)

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()


    ## collision with wall
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce("wall")


    ## collision with paddle
    if ball.distance(right_paddle) < 25 and ball.xcor() >320 or ball.distance(left_paddle) < 25 and ball.xcor() < -320:
        ball.bounce("paddle")
        
        ## miss ball
    if ball.xcor() > 390:
        ball.resetPosition()
        scoreboard.point("left")
    elif ball.xcor() < -390:
        scoreboard.point("right")
        ball.resetPosition()



screen.exitonclick()

