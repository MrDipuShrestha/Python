import turtle
from turtle import Screen
from board import Board
import  time

screen = Screen()
screen.setup(width=600, height=600)
screen.title("tic-tac-toe")
screen.bgcolor("white")
screen.tracer(0)

board = Board()

board.draw_vertical_grid()
board.draw_horizontal_grid()
screen.update()
time.sleep(0.1)

screen.listen()
screen.onscreenclick(board.click_handler)

turtle.mainloop()
