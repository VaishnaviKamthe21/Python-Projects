STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.go_to_start()
        self.left(90)
        

    def move(self):
        new_y=self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(),new_y)
    
    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def detect_finish(self):
        if self.ycor()>=FINISH_LINE_Y:
            return True
        else:
            return False

    # def update_score(self):
    #     scoreboard.update_scoreboard(self.score)
    #     if self.ycor()>=FINISH_LINE_Y:
    #         self.score+=1
    #         self.goto(STARTING_POSITION)
    #         car_manager.increase_speed()

    


            
            

        
