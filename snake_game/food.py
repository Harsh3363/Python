from turtle import Turtle
import random


# inheriting from food class from Turtle class ------>
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        # the normal size is 20*20 but we are multiplying it by 0.5 which means now it's 10*10 ---->
        self.shapesize(0.5, 0.5)
        self.color("blue")
        self.speed("fastest")
        self.food_location()

    def food_location(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.setpos(random_x, random_y)