# ----------------------------------+
# Shengnan Zhou                     |
# CSCI 107, Assignment 7            |
# Last Updated: March 26, 2018      |
# ----------------------------------|
# Use while loops to create a       |
# random generated number of dots   |
# with random color, and user needs |
# to guess the correct number of    |
# dots.                             |
# ----------------------------------+




import random
import turtle





# Setup
dots = turtle.Turtle()
wn = turtle.Screen()
wn.setworldcoordinates(0,0,400,400)
dots.speed(0)



def movedot():
    x = random.randint(5,396)
    y = random.randint(5,396)
    dots.penup()
    dots.goto(x,y)
    dots.pendown()





# Draw dots
number = random.randint(50,201)
start = 0

while start <= number:
    movedot()
    color = random.choice(["red", "blue", "yellow", "orange", "green", "purple"])
    dots.dot(10,color)
    start = start + 1




# User guess
guess = int(input("Guess the number of dots. Must be between 50 and 200: "))
a = 1
while guess != number:
    if guess < 50 or guess > 200:
        print("The number you guessed,", guess, ",is out of range. Try again")
        guess = int(input("Guess the number of dots. Must be between 50 and 200: "))
    elif guess < number:
        print("Your guess was too low. Try again")
        guess = int(input("Guess the number of dots. Must be between 50 and 200: "))
        a = a + 1
    elif guess > number:
        print("Your guess was too high. Try again")
        guess = int(input("Guess the number of dots. Must be between 50 and 200: "))
        a = a + 1

print("You guessed the correct value after", a, "guess")


















