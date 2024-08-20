from turtle import Turtle
import random

COLORS = ["red", "green", "blue", "orange", "yellow", "purple"]
STARTING_MOVING_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVING_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_turtle = Turtle()
            new_turtle.shape("square")
            new_turtle.color(random.choice(COLORS))
            new_turtle.penup()
            new_turtle.turtlesize(stretch_wid=1, stretch_len=3)
            random_y = random.randint(-260, 260)
            new_turtle.goto(300, random_y)
            self.all_cars.append(new_turtle)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
