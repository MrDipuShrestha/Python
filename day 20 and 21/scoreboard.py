from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 18, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", "r") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_score()
        self.hideturtle()
        self.is_game_on = True

    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score} High Score : {self.high_score}", align=ALIGNMENT, font=FONT)

    def restart(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()
        self.is_game_on = True

    # def game_over(self):
    #     self.is_game_on = False
    #     self.goto(0, 0)
    #     self.write("GAME OVER!", align=ALIGNMENT, font=FONT)
    #     self.goto(0, -30)
    #     self.write("Press enter to start again", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()
