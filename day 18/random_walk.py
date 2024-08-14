import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
# color = ["medium blue", "peru", "lawn green", "blanched almond", "indigo", "dark slate blue"]

turtle.colormode(255)
def RandomColor():
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)

    color_tuple = (red, green, blue)
    return color_tuple

direction = [0, 90, 180, 270]

for _ in range(200):
    tim.pensize(10)
    # tim.pencolor(random.choice(color))
    tim.pencolor(RandomColor())
    tim.forward(30)
    tim.setheading(random.choice(direction))

screen = Screen()
screen.exitonclick()