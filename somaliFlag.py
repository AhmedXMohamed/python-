import turtle
import time

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("blue")

# Create a turtle for drawing the star
star_turtle = turtle.Turtle()
star_turtle.speed(2)
star_turtle.color("white")
star_turtle.penup()
star_turtle.goto(-30, 20)
star_turtle.pendown()

# Function to draw a five-pointed star
def draw_star():
    for _ in range(5):
        star_turtle.forward(60)
        star_turtle.right(144)

# Draw the star initially
draw_star()

# Animation loop
while True:
    # Clear the star
    star_turtle.clear()

    # Move to a new position
    x, y = star_turtle.position()
    star_turtle.goto(x + 10, y - 10)

    # Draw the star again
    draw_star()

    # Update the screen
    screen.update()

    # Pause for a short time
    time.sleep(0.2)

# Uncomment the following line if you want to run the animation in an IDE that supports turtle graphics
# turtle.mainloop()
