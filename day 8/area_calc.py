# 1 can of paint can pain t 5 sq. meter of wall

import math

def no_of_paints(height, width, cover):
    total_can = math.ceil((height * width) / cover)

    print(f"You need {total_can} of cans to paint the wall.")


height_wall = int(input("Enter the height of the wall: "))
width_wall = int(input("Enter the width of the wall: "))
coverage = 5

no_of_paints(height = height_wall, width = width_wall, cover = coverage)

