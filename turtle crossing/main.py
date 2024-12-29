import time
from turtle import Screen
from scoreboard import Scoreboard
from player import Player
from car_manager import CarManager

score=0

screen = Screen()
screen.listen()
screen.setup(width=600, height=600)
screen.tracer(0)

p1=Player()
screen.onkey(p1.move,'Up')

car_manager=CarManager()

scoreboard=Scoreboard()
scoreboard.update_scoreboard(score)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.generate_car()
    car_manager.move_cars()

    #detect collision
    for car in car_manager.list_of_cars:
        if car.distance(p1)<20:
            game_is_on=False
            scoreboard.gameover_text()

    if p1.detect_finish():
        p1.go_to_start()
        score+=1
        scoreboard.update_scoreboard(score)
        car_manager.increase_speed()

screen.exitonclick()
