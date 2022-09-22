from turtle import Turtle
FONT = ("Courier",15,"normal")


class Score(Turtle):
    def __init__(self):
        self.point = 0
        super().__init__()
        self.setposition(0,275)
        self.hideturtle()
        self.color("white")
        self.write(f"score: {self.point}",font=("Arial",15,"normal"))


    def refresh_score(self):
        self.point += 1
        self.clear()
        self.write(f"score: {self.point}",font=FONT)


