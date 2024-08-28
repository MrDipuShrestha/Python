from turtle import Turtle
RANGE = [-80, 80]
FROM = 300
TO = -300


class Board(Turtle):
    def __init__(self):
        super().__init__()
        self.pensize(3)
        self.hideturtle()

    def draw_vertical_grid(self):
        for i in RANGE:
            self.penup()
            self.goto(i, FROM)
            self.pendown()
            self.goto(i, TO)

    def draw_horizontal_grid(self):
        for i in RANGE:
            self.penup()
            self.goto(FROM, i)
            self.pendown()
            self.goto(TO, i)