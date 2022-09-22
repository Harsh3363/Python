import turtle
import time
from snake import Snake
from food import Food
from scoreboard import Score

screen = turtle.Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake game")

screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    # this time.speed(1) for slowing down the animation
    time.sleep(0.1)
    snake.move()

    #     detecting collision between food and snake ->
    if snake.snake_first_square.distance(food) < 15:
        food.food_location()
        score.refresh_score()

screen.exitonclick()
