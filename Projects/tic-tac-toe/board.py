from turtle import Turtle

RANGE = [-80, 80]
FROM = 300
TO = -300


class Board(Turtle):
    def __init__(self):
        super().__init__()
        self.pensize(3)
        self.hideturtle()
        self.grid = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

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

    def click_handler(self, x, y):
        row = int((150 - y) // 200)
        col = int((150 + x) // 200)
        print(f"x-cor = {x}, y-chor={y}")
        self.goto(row, col)
        self.write(f"{self.current_player}", font=("Arial", 20, "normal"))

