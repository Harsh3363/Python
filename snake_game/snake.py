import turtle

POS = [0, 20, 40]
FORWARD_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.snake_first_square = self.segment[0]

    def create_snake(self):
        for pos in POS:
            timmy2 = turtle.Turtle("square")
            timmy2.penup()
            timmy2.color("white")
            timmy2.setx(pos)
            self.segment.append(timmy2)

    def create_snake_point(self):
        for pos in POS:
            timmy2 = turtle.Turtle("square")
            timmy2.penup()
            timmy2.color("white")
            timmy2.setx(pos)
            self.segment.append(timmy2)

    def move(self):
        # below lines of code for moving all the blocks of square in sequence ->>>>>>>>
        for seg_num in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg_num - 1].xcor()
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x, new_y)
        self.snake_first_square.forward(FORWARD_DISTANCE)

    def up(self):
        # heading function will give an angle in numbers and then to check if it's in up,down,right,left direction
        if self.snake_first_square.heading() != DOWN:
            self.snake_first_square.setheading(UP)

    def down(self):
        if self.snake_first_square.heading() != UP:
            self.snake_first_square.setheading(DOWN)

    def right(self):
        if self.snake_first_square.heading() != LEFT:
            self.snake_first_square.setheading(RIGHT)

    def left(self):
        if self.snake_first_square.heading() != RIGHT:
            self.snake_first_square.setheading(LEFT)
