COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

import random
from turtle import Turtle


class CarManager:
    def __init__(self):
        self.list_of_cars= []
        self.speed=STARTING_MOVE_DISTANCE

    def generate_car(self):
        random_chance=random.randint(1,6)
        if random_chance==1:
            new_car= Turtle(shape="square")
            new_car.shapesize(stretch_len=2,stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y=random.randint(-250,250)
            new_car.goto(300,random_y)
            self.list_of_cars.append(new_car)

    def move_cars(self):
        for car in self.list_of_cars:
            car.backward(self.speed)
    
    def increase_speed(self):
        self.speed+=MOVE_INCREMENT

    

    

