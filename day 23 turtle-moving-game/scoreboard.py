from turtle import Turtle

FONT = ('Courier', 24, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.score()

    def score(self):
        self.clear()
        self.write(f"Level:{self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", align="center", font=FONT)