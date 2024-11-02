SCORE=0
ALIGN="center"
FONT=('Arial', 24, 'normal')
SCOREBOARD_XCOR=0
SCOREBOARD_YCOR=250
from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.score_counter=SCORE
        self.high_score=0
        self.color("white")
        self.goto(SCOREBOARD_XCOR,SCOREBOARD_YCOR)
        self.hideturtle()
        self.write(arg=f"Score: {self.score_counter} HIGH SCORE: {self.high_score}", move=False, align=ALIGN, font=FONT)
        
    
    def update_score(self):
        self.clear()
        
        self.write(arg=f"SCORE: {self.score_counter} HIGH SCORE: {self.high_score} ", move=False, align=ALIGN, font=FONT)
        self.score_counter+=1

    def reset(self):
        if self.score_counter > self.high_score:
            self.high_score=self.score_counter
        self.score_counter=0
        self.update_score()

    

        
