from turtle import Turtle,Screen
from random import randint

screen=Screen()
screen.setup(500,400)
bet=screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color: ")
colors=['red','orange','yellow','green','blue','purple']
kachuas=[]
y=[-150,-100,-50,0,50,100]
race_on=True

for i in range(0,6):
    new_turtle=Turtle(shape='turtle')
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(-230,y[i])
    kachuas.append(new_turtle)

while race_on:
    for turtle in kachuas:
        if turtle.xcor()>220:
            winner=turtle.pencolor()
            if winner==bet:
                print("Your turtle wins!!")
            else:
                print(f"You lost! The {winner} turtle won the race")
            race_on=False
    
        turtle.forward(randint(0,10))

screen.exitonclick()