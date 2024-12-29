from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen=Screen()

#setting up screen
screen.setup(width=800,height=600)
screen.bgcolor('black')
screen.title("Pong")
screen.tracer(0)

r_paddle=Paddle(350)
l_paddle=Paddle(-350)

scoreboard=Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

ball=Ball()

game_on = True
while game_on:
    time.sleep(ball.movement_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 60 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() > -340:
        ball.bounce_x()
        

    if ball.xcor()>380:
        ball.reset_position()
        scoreboard.l_score_up()
    
    if ball.xcor()<-380:
        ball.reset_position()
        scoreboard.r_score_up()

    
screen.exitonclick()


