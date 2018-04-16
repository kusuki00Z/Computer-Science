# -----------------------------------------+
# Shengnan Zhpu, Alex Tseng                |
# CSCI 107, Assignment 9                   |
# Last Updated: April 16, 2018             |
# -----------------------------------------|
# Draw recursive squares.                  |
# -----------------------------------------+

import turtle
import random


# Setup

square = turtle.Turtle()
square.hideturtle()
square.speed(0)

window = turtle.Screen()
window.colormode(255)

print("Recursive Squares Program")
print("-------------------------")
level = int(input("Enter the level of recursion from 1 to 7: "))
side_length = int(input("Enter the length of a side from 200 to 600: "))

# --------------------------------------------------------------------------- #



# draw square function
def draw_squares(t, left_x, top_y, length, level):
    # random color
    r = random.randrange(0,256)
    g = random.randrange(0,256)
    b = random.randrange(0,256)
    t.fillcolor(r,g,b)

    t.up()
    t.goto(left_x, top_y)
    t.down()
    t.begin_fill()
    for i in range(4):
        t.forward(length)
        t.right(90)
    t.end_fill()


    # recursive
    if level > 1:
        draw_squares(t, left_x, top_y, length/2, level-1)
        draw_squares(t, left_x+length/2, top_y-length/2, length/2, level-1)





draw_squares(square, -side_length/2, side_length/2, side_length, level)


window.exitonclick()
