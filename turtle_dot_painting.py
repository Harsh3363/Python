import turtle
import random

timmy = turtle.Turtle()
screen = turtle.Screen()

timmy.hideturtle()
timmy.penup()
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
timmy.speed("fastest")
# timmy.pensize(7)
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colors = (r,g,b)
    return random_colors


def drawdot(space, x):
    for i in range(x):
        for j in range(x):
            # timmy.color(random_color())
            timmy.dot(10,random_color())

            timmy.forward(space)
        timmy.backward(space * x)

        timmy.left(90)
        timmy.forward(space)
        timmy.right(90)


timmy.penup()
drawdot(25, 12)

timmy.hideturtle()
screen.exitonclick()
