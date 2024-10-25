from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.speed(0)
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.move_food()
        
    def move_food(self):
        x_cor=random.randint(-280,280)
        y_cor=random.randint(-280,280)
        self.goto(x_cor,y_cor)
