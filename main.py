from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import Score
import time
display = Screen()
display.setup(width=600, height=600)
display.title("Snake Game")
display.bgcolor("black")
display.tracer(0)
is_game_on = True
snake=Snake()
apple=Food()
score=Score()
display.listen()
display.onkeypress(snake.move_up, "w")
display.onkeypress(snake.move_right, "d")
display.onkeypress(snake.move_left, "a")
display.onkeypress(snake.move_down, "s")
while is_game_on:
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()
    display.update()
    time.sleep(0.1)
    snake.move_snake()
    display.update()
    if  snake.head.distance(apple)<15:
        apple.move_food()
        snake.extend()
        score.update_score()
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            score.reset()
            snake.reset()

score.game_over()
display.exitonclick()