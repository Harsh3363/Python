import turtle
import random

screen = turtle.Screen()

screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make your bet",prompt="which one will win?")
game = False
# print(user_bet)
colors = ["red","yellow","blue","orange","green","purple"]

new_turtle = []

for i in range(0,6):
    timmy = turtle.Turtle("turtle")
    # timmy.shape("turtle")
    timmy.color(colors[i])
    timmy.penup()
    timmy.goto(-240,-100+i*40)
    new_turtle.append(timmy)

if user_bet:
    game = True

while game:
    for turtle in new_turtle:
        if turtle.xcor()>230:
            winning_color = turtle.pencolor()
            game=False
            if winning_color==user_bet:
                print(f"congrats you won, the winning colors is {winning_color}")
            else:
                print(f"You loose, the winning colors is {winning_color}")
        trt_for = random.randint(0,10)
        turtle.forward(trt_for)

screen.exitonclick()
