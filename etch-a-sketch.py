from turtle import Turtle, Screen

kachua=Turtle()
screen=Screen()

def move():
    kachua.forward(10)

def turn_right():
    kachua.right(10)

def turn_left():
    kachua.left(10)

def move_back():
    kachua.back(10)

def reset():
    kachua.reset()
    
screen.onkey(fun=move,key='w')
screen.onkey(fun=turn_left,key='a')
screen.onkey(fun=turn_right,key='d')
screen.onkey(fun=move_back,key='s')
screen.onkey(fun=reset,key='c')

screen.listen()
screen.exitonclick()