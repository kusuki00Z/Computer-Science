# -----------------------------------------+
# Shengnan Zhou                            |
# CSCI 107, Assignment 5                   |
# Last Updated: February 25, 2018          |
# -----------------------------------------|
# Use loops and functions to draw a tile   |
# map                                      |
# -----------------------------------------+



import turtle

wn = turtle.Screen()
tile = turtle.Turtle()
tile.speed(0)





# Move function to move the turtle
def moveTile(someturle,x,y,angle):
    someturtle.penup()
    someturtle.goto(x,y)
    someturtle.setheading(angle)
    someturtle.pendown()



# Draw function to draw the tile
def drawTile(someturtle,pen,fill):
    someturtle.pencolor(pen)
    someturtle.fillcolor(fill)
    someturtle.begin_fill()
    for i in range(4):
        someturtle.forward(10)
        someturtle.right(90)
    someturtle.end_fill()


drawTile(tile,"red","blue")
wn.exitonclick()
