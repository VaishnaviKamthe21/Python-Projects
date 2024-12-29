from turtle import Turtle


STARTING_POSI=[(0,0),(-20,0),(-40,0)]
MOVE_DIST=20
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self):
        self.my_snake=[]
        self.create_snake()
        self.head=self.my_snake[0]

    def create_snake(self):
        for posi in STARTING_POSI:
            self.add_segment(posi)

    def add_segment(self,position):
        new_segment=Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.my_snake.append(new_segment)

    def extend(self):
        self.add_segment(self.my_snake[-1].position())

    def move(self):
        for seg_num in range(len(self.my_snake)-1,0,-1):
            x=self.my_snake[seg_num - 1].xcor()
            y=self.my_snake[seg_num - 1].ycor()
            self.my_snake[seg_num].goto(x,y)

        self.head.forward(MOVE_DIST)

    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)