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


def snake_game():
    game_is_on = True
    while game_is_on:
        screen.update()
        # this time.speed(1) for slowing down the animation
        time.sleep(0.1)
        snake.move()

        #     detecting collision between food and snake ->
        if snake.snake_first_square.distance(food) < 15:
            food.food_location()
            snake.extend_snake()
            score.refresh_score()

        #     below lines of code is to detect the collision of snake with the wall ------->
        if snake.snake_first_square.xcor() > 290 or snake.snake_first_square.xcor() < -290 or snake.snake_first_square.ycor() > 280 or snake.snake_first_square.ycor() < -280:
            game_is_on = False
            score.game_over()
            # user_bet = screen.textinput(title="You want to play again", prompt="yes or no")
        #     detect collision with snake tail -------->
        #     slicing the segment list ignore item at 0th index to last item
        for seg in snake.segment[1:]:
            if snake.snake_first_square.distance(seg) < 5:
                game_is_on = False
                score.game_over()
                # user_bet = screen.textinput(title="You want to play again", prompt="yes or no")


snake_game()
screen.exitonclick()
