#BH 2nd Turtle Racing

no_winner = True
winner = None

#Import the turtle and random libraries at the beginning

import turtle
import random

#Clearly mark the finish line on the screen

screen = turtle.Screen()
screen.setup(500,500)

def draw_finish_line():
    line = turtle.Turtle()
    line.shape("classic")
    line.color("black")
    line.pencolor("black")
    line.penup()
    line.goto(400,-500)
    line.right(270)
    line.pendown()
    line.forward(1000)
    del line
draw_finish_line()

#Create a game with 5 turtles, each a different color
def create_turtles():
    global red_turtle, orange_turtle, yellow_turtle, green_turtle, indigo_turtle
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
    red_turtle.penup()
    orange_turtle.penup()
    yellow_turtle.penup() 
    green_turtle.penup()
    indigo_turtle.penup() 
    red_turtle.setpos(0,300)
    orange_turtle.setpos(0,150)
    yellow_turtle.setpos(0,0)
    green_turtle.setpos(0,-150)
    indigo_turtle.setpos(0,-300)
    red_turtle.pendown()
    orange_turtle.pendown()
    yellow_turtle.pendown()
    green_turtle.pendown()
    indigo_turtle.pendown()
create_turtles()

def move_turtles():
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
def the_winner():
    if no_winner == False:
        #Announce the winner either on the turtle screen or in the terminal
        print("The winner is the", winner, "!")
    else:
        pass

#Use a loop to move turtles forward a random number of steps each round

while no_winner:
    move_turtles()
    if red_turtle.xcor() > 400:
        winner = "red turtle"
        no_winner = False
    elif orange_turtle.xcor() > 400:
        winner = "orange turtle"
        no_winner = False
    elif yellow_turtle.xcor() > 400:
        winner = "yellow turtle"
        no_winner = False
    elif green_turtle.xcor() > 400:
        winner = "green turtle"
        no_winner = False
    elif indigo_turtle.xcor() > 400:
        winner = "indigo turtle"
        no_winner = False
    the_winner()



turtle.done()

#Make sure the turtles' movement and race logic are correctly implemented