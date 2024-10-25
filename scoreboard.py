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
        self.color("white")
        self.goto(SCOREBOARD_XCOR,SCOREBOARD_YCOR)
        self.hideturtle()
        self.write(arg=f"Score: {self.score_counter} ", move=False, align=ALIGN, font=FONT)
        
    
    def update_score(self):
        self.clear()
        self.score_counter+=1
        self.write(arg=f"Score: {self.score_counter} ", move=False, align=ALIGN, font=FONT)

    def game_over(self):
        self.home()
        self.write(arg=f"GAME OVER!", move=False, align=ALIGN, font=('Arial', 30, 'bold'))
        
