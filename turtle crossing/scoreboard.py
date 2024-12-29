FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-220,260)

    def update_scoreboard(self,score):
        self.clear()
        self.write(f"Level: {score}",align="center",font=FONT)

    def gameover_text(self):
        gameover=Turtle()
        gameover.hideturtle()
        gameover.penup()
        gameover.write("Game Over",align='center',font=FONT)
