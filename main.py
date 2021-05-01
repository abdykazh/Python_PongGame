from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My pong game!")
screen.tracer(0)

paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle_l.up, "w")
screen.onkey(paddle_l.down, "s")
screen.onkey(paddle_r.up, "Up")
screen.onkey(paddle_r.down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with a wall
    if ball.ycor() > 288 or ball.ycor() < -288:
        ball.bounce_y()

    #Detect collision with the paddle
    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 or ball.xcor() < -320:
        ball.bounce_x()
    elif ball.xcor() > 380:
        ball.reset()
        scoreboard.l_point()
    elif ball.xcor() < -380:
        ball.reset()
        scoreboard.r_point()

screen.exitonclick()