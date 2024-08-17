from turtle import Turtle, Screen

tim = Turtle()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def turn_left():
    # tim.left(10)
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)
def turn_right():
    # tim.right(10)
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)
def clear_screen():
    # tim.reset()
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen = Screen()
screen.listen()
screen.onkey(move_forward,"Up")
screen.onkey(move_backward,"Down")
screen.onkey(turn_left,"Left")
screen.onkey(turn_right,"Right")
screen.onkey(clear_screen,"c")

screen.exitonclick()