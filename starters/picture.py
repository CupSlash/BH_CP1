#BH 2nd Picture
import turtle

def draw_branch(length):
    if length > 5:
        for i in range(3):
            turtle.forward(length)
            draw_branch(length / 3)
            turtle.backward(length)
            turtle.right(60)

turtle.speed()
turtle.pencolor("light blue")
turtle.penup()
turtle.setpos(0,0)
turtle.pendown()

def snowflake():
    for i in range():
        draw_branch(100)
        turtle.right(60)

snowflake()

turtle.hideturtle()
