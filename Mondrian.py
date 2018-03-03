# -----------------------------------------+
# Shengnan Zhou, Alex Tseng                |
# CSCI 107, Assignment 5                   |
# Last Updated: March 04, 2018             |
# -----------------------------------------|
# Use loops, functions, and different      |
# modules to randomly generate a           |
# Mondrian-like art with user input the    |
# number and the maximum size of           |
# rectangles.                              |
#                                          |
# -----------------------------------------+



import turtle
import math
import random



# Setup
wn = turtle.Screen()
rectangle = turtle.Turtle()
rectangle.speed(0)
wn.bgcolor("black")
wn.colormode(255)



# User input
amount = wn.numinput("Number of rectangles",
                    "Enter the number of the rectangle to be drawn:",
                    20, minval=1, maxval=500)

max_width = wn.numinput("Maximum width of rectangles",
                    "Enter the maximum width of the rectangle:",
                    10, minval=1, maxval=200)

max_height = wn.numinput("Maximun height of the rectangles",
                     "Enter the maximum height of the rectangle:",
                     10, minval=1, maxval=200)



# Function to draw rectangle
def drawRectangle(someturtle,w,h,r_val,g_val,b_val):
    someturtle.pencolor(r_val,g_val,b_val)
    someturtle.fillcolor(r_val,g_val,b_val)
    someturtle.begin_fill()
    for i in range(2):
        someturtle.forward(w)
        someturtle.right(90)
        someturtle.forward(h)
        someturtle.right(90)
    someturtle.end_fill()



# Function to move turtle
def moveTurtle(someturtle,x_pos,y_pos,angle):
    someturtle.penup()
    someturtle.goto(x_pos,y_pos)
    someturtle.pendown()
    someturtle.setheading(angle)





# Drawing rectangles randomly
for i in range(int(amount)):
    width = max(10, random.randrange(int(max_width)))
    height = max(10, random.randrange(int(max_height)))
    x = random.uniform(-300,200)
    y = random.uniform(-200,300)
    r = random.randrange(0,256)
    g = random.randrange(0,256)
    b = random.randrange(0,256)
    drawRectangle(rectangle,width,height,r,g,b)
    moveTurtle(rectangle,x,y,0)




# Clean up
rectangle.hideturtle()
wn.exitonclick()
