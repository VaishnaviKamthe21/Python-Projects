from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("./Beginner-Python-Projects/snake_game.py/data.txt") as data:
            self.highscore=int(data.read())
        self.color("white")
        self.penup()
        self.goto(0,260)
        self.hideturtle()
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} \t Highscore: {self.highscore}", align="center", font=("Arial",24,"normal"))

    def reset(self):
        if self.score>self.highscore:
            self.highscore = self.score
            with open("data.txt","w") as data:
                data.write(str(self.highscore))
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over", align="center", font=("Arial",24,"normal"))

    def increase_score(self):
        self.score+=1
        self.update_scoreboard()