import turtle
t = turtle.Pen()

import turtle

# Set up the turtle screen
turtle.bgcolor("lightblue")
turtle.title("Somali Flag")
turtle.speed(2)
turtle.hideturtle()

# Draw the flag
turtle.penup()
turtle.goto(-100, 60)
turtle.pendown()
turtle.color("white")
turtle.begin_fill()
for _ in range(5):
    turtle.forward(200)
    turtle.right(144)
turtle.end_fill()

# Hide the turtle window when clicked
turtle.exitonclick()
