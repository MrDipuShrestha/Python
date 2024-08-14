import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()


turtle.colormode(255)
def RandomColor():
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)

    color_tuple = (red, green, blue)
    return color_tuple

def draw_spirograph(size_of_gap):
    tim.speed(0)
    for _ in range(int(360/size_of_gap)):
        tim.pencolor(RandomColor())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)

screen = Screen()
screen.exitonclick()