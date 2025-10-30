#BH 2nd Turtle Racing

no_winner = True

#Import the turtle and random libraries at the beginning

import turtle
import random

#Clearly mark the finish line on the screen

screen = turtle.Screen()
screen.setup(500,500)

pen = turtle.Turtle()
pen.shape("classic")
pen.color("black")
pen.pencolor("black")
pen.penup()
pen.goto(400,-500)
pen.right(270)
pen.pendown()
pen.forward(1000)
del pen

#Create a game with 5 turtles, each a different color

red_turtle = turtle.Turtle()
orange_turtle = turtle.Turtle()
yellow_turtle = turtle.Turtle()
green_turtle = turtle.Turtle()
indigo_turtle = turtle.Turtle()

red_turtle.shape("turtle")
orange_turtle.shape("turtle")
yellow_turtle.shape("turtle")
green_turtle.shape("turtle")
indigo_turtle.shape("turtle")

red_turtle.color("red")
orange_turtle.color("orange")
yellow_turtle.color("yellow")
green_turtle.color("green")
indigo_turtle.color("indigo")

red_turtle.setpos(0,300)
orange_turtle.setpos(0,150)
yellow_turtle.setpos(0,0)
green_turtle.setpos(0,-150)
indigo_turtle.setpos(0,-300)

#Use a loop to move turtles forward a random number of steps each round

while no_winner:
    indigo_steps = random.randint(1,39)
    green_steps = random.randint(1,39)
    yellow_steps = random.randint(1,39)
    orange_steps = random.randint(1,39)
    red_steps = random.randint(1,39)
    red_turtle.forward(red_steps)
    orange_turtle.forward(orange_steps)
    yellow_turtle.forward(yellow_steps)
    green_turtle.forward(green_steps)
    indigo_turtle.forward(indigo_steps)
    if red_turtle.xcor() > 400:
        winner = {True, red_turtle}
    elif orange_turtle.xcor() > 400:
        winner = {True,orange_turtle}
    elif yellow_turtle.xcor() > 400:
        winner = {True,yellow_turtle}
    elif green_turtle.xcor() > 400:
        winner = {True,green_turtle}
    elif indigo_turtle.xcor() > 400:
        winner = {True, indigo_turtle}
    else:
        pass
    if winner[0]:
        no_winner = False
        #Announce the winner either on the turtle screen or in the terminal
        print("The winner is", winner[1], "!")
    else:
        pass


turtle.done()
#Make sure the turtles' movement and race logic are correctly implemented
#Use functions to organize code, e.g., one for setting up the race, one for moving turtles, and one for determining the winner
#Test the game to ensure it runs smoothly and correctly identifies the winner (minimum of 5 times)
#Commit and push your code to Github