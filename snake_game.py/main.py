from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen=Screen()

#setting up screen
screen.setup(600,600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

#creating snake
snake=Snake()
#serving food
food=Food()
#displaying score
score_board=ScoreBoard()
#taking input from keyboard
screen.listen()

#snakes movements
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_on=True

while game_on:
    #update screen every 0.1sec
    screen.update()
    time.sleep(0.1)

    snake.move()

    #detect collision with food and update score
    if snake.head.distance(food) < 15:
        food.refresh()
        score_board.increase_score()
        snake.extend()

    #detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 280 or snake.head.ycor() < -290:
        score_board.reset()
        snake.reset()
        # game_on=False
        # score_board.game_over()
        
    #detect collision with tail
    for segment in snake.my_snake[1:]:
        if snake.head.distance(segment) < 10:
            score_board.reset()
            snake.reset()
            # game_on=False
            # score_board.game_over()



screen.exitonclick()