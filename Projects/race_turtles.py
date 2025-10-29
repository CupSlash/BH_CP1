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

indigo_steps = random.randint(1,10)
green_steps = random.randint(1,10)
yellow_steps = random.randint(1,10)
orange_steps = random.randint(1,10)
red_steps = random.randint(1,10)

while no_winner:
    red_turtle.forward(red_steps)
    orange_turtle.forward(red_steps)
    yellow_turtle.forward(red_steps)
    green_turtle.forward(red_steps)
    indigo_turtle.forward(red_steps)
    if red_turtle in (400, 300):
        winner = red_turtle
        no_winner = False
    if red_turtle in (400, 300):
        winner = red_turtle
        no_winner = False
    if red_turtle in (400, 300):
        winner = red_turtle
        no_winner = False
    if red_turtle in (400, 300):
        winner = red_turtle
        no_winner = False
    if red_turtle in (400, 300):
        winner = red_turtle
        no_winner
    else:
        pass


#Announce the winner either on the turtle screen or in the terminal

print("The winner is", winner, "!")

#Make sure the turtles' movement and race logic are correctly implemented
#Use functions to organize code, e.g., one for setting up the race, one for moving turtles, and one for determining the winner
#Test the game to ensure it runs smoothly and correctly identifies the winner (minimum of 5 times)
#Commit and push your code to Github