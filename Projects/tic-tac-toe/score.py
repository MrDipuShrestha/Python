from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.grid = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
