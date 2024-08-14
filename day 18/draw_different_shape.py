from turtle import Turtle, Screen
import random

tim = Turtle()
color = ["medium blue", "peru", "lawn green", "blanched almond", "indigo", "dark slate blue"]
def DrawShape(no_of_sides, rand_color):
    angle = 360 / no_of_sides
    tim.color(rand_color)
    for _ in range(no_of_sides):
        tim.forward(100)
        tim.right(angle)

for i in range (3,10):
    rand_color  = random.choice(color)
    DrawShape(i, rand_color)

screen = Screen()
screen.exitonclick()