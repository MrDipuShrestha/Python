from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(height=600, width=600)
screen.title("Turtle Moving Game")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(player.move, "Up")
screen.onkey(player.move_back, "Down")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()

    # detect collision with cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # detect successful cross
    if player.is_gone_to_finish_line():
        player.goto_start()
        car_manager.level_up()
        scoreboard.increase_level()


screen.exitonclick()
