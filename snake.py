STARTING_POSITION=[(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
RIGHT=0
LEFT=180


from turtle import Turtle, Screen
class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]

    def create_snake(self):
        for pos in STARTING_POSITION:
            self.add_segment(pos)
            
    def add_segment(self, pos):
        new_segment=Turtle(shape="square")
        new_segment.color("white")
        new_segment.pu()
        new_segment.goto(pos)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move_snake(self):
            for seg_num in range(len(self.segments)-1,0,-1):
                newx=self.segments[seg_num-1].xcor()
                newy=self.segments[seg_num-1].ycor()
                self.segments[seg_num].goto(newx,newy)
            self.segments[0].fd(MOVE_DISTANCE)
    def move_up(self):
        if self.head.heading()!=DOWN:
            self.segments[0].seth(UP)
    def move_down(self):
        if self.head.heading()!=UP:
            self.segments[0].seth(DOWN)
    def move_right(self):
        if self.head.heading()!=LEFT:
            self.segments[0].seth(RIGHT)
    def move_left(self):
        if self.head.heading()!=RIGHT:
            self.segments[0].seth(LEFT)
    
    