from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_input = screen.textinput(title="Do a bet", prompt="Which turtle will win the race? Enter the color: ")
color = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtle = []

for index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color[index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[index])
    all_turtle.append(new_turtle)

if user_input:
    is_race_on = True

while is_race_on:

    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_input:
                print(f"You've won! The {winning_color} turtle won the race.")
            else:
                print(f"You've lost! The {winning_color} turtle won the race.")

        random_move = random.randint(0, 10)
        turtle.forward(random_move)


screen.exitonclick()