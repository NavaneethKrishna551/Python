import turtle
import random
import math
import shapes
from time import sleep
#currently working and main features completed


# Imports necessary libraries
# import shapes (Uncomment this if you have a shapes module)

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Navaneeth Krishna")

# Creates a window with given properties

usertext = ""  # Initialize usertext variable globally
used_positions = []  # List to keep track of used positions
drawn_turtles = []
 # List to keep track of user-drawn turtles

def instruction():
    tutel.goto(0, 0)
    tutel.write("Go full screen", font=("calibri", 50, "normal"))
    sleep(1.5)
    tutel.clear()

def writing():
    global usertext
    print("working")
    usertext = screen.textinput("Writing...", "What do you want to write?")

def get_unique_position():
    while True:
        pen_x = random.randrange(-300, 200)
        pen_y = random.randrange(-200, 300)
        position = (pen_x, pen_y)
        if all(math.dist(position, prev_pos) > 50 for prev_pos in used_positions):  # Ensure no overlap
            used_positions.append(position)
            return position

def button(button_action, btn_text, btnloc_x, btnloc_y):
    btn = turtle.Turtle()
    btn.color("gray")
    btn.shape("square")
    btn.shapesize(1, 2)
    btn.penup()
    btn.goto(btnloc_x, btnloc_y + 15)
    btn.write(btn_text, align="center", font=("arial", 15, "normal"))
    btn.color("white")
    btn.goto(btnloc_x, btnloc_y)  # Move the turtle to avoid text overlap
    btn.onclick(button_action)

# Key binding for writing
screen.onkeypress(writing, "w")
screen.listen()

# Create a turtle for writing
tutel = turtle.Turtle()
tutel.speed(10)
tutel.hideturtle()
tutel.pendown()
tutel.color("white")


# Create another turtle for drawing
drawer = turtle.Turtle()
drawer.speed(10)
drawer.hideturtle()
drawer.color("white")
drawer.penup()



def button_shape_polygon(x, y):
    sides = int(screen.textinput("Drawing...", "How many sides do you want for the polygon?"))
    length = int(screen.textinput("Drawing...", "What length do you want for the polygon?"))
    position_x = int(screen.textinput("Drawing...", "What x position do you want your shape to be at?"))
    position_y = int(screen.textinput("Drawing...", "What y position do you want your shape to be at?"))
    drawer_turtle = turtle.Turtle()
    drawer_turtle.color("white")
    drawer_turtle.penup()
    drawer_turtle.goto(position_x, position_y)
    drawer_turtle.pendown()
    shapes.polygon(drawer_turtle, length, sides)
    drawer_turtle.hideturtle()
    drawn_turtles.append(drawer_turtle)

def button_shape_circle(x, y):
    radius = int(screen.textinput("Drawing...", "What radius do you want for the circle?"))
    position_x = int(screen.textinput("Drawing...", "What x position do you want your shape to be at?"))
    position_y = int(screen.textinput("Drawing...", "What y position do you want your shape to be at?"))
    drawer_turtle = turtle.Turtle()
    drawer_turtle.color("white")
    drawer_turtle.penup()
    drawer_turtle.goto(position_x, position_y)
    drawer_turtle.pendown()
    shapes.circle(drawer_turtle, radius)
    drawer_turtle.hideturtle()
    drawn_turtles.append(drawer_turtle)

def button_shape_arc(x, y):
    radius = int(screen.textinput("Drawing...", "What radius do you want for the arc?"))
    angle = int(screen.textinput("Drawing...", "What angle do you want for the arc?"))
    position_x = int(screen.textinput("Drawing...", "What x position do you want your shape to be at?"))
    position_y = int(screen.textinput("Drawing...", "What y position do you want your shape to be at?"))
    drawer_turtle = turtle.Turtle()
    drawer_turtle.color("white")
    drawer_turtle.penup()
    drawer_turtle.goto(position_x, position_y)
    drawer_turtle.pendown()
    shapes.arc(drawer_turtle, radius, angle)
    drawer_turtle.hideturtle()
    drawn_turtles.append(drawer_turtle)

def button_clear(x, y):
    for turtle in drawn_turtles:
        turtle.clear()
        turtle.hideturtle()
    drawn_turtles.clear()

instruction()

# Create buttons
button(button_clear, "!CLEAR!", -365, 250)
button(button_shape_polygon, "polygon", 365, 250)
button(button_shape_circle, "circle", 305, 250)
button(button_shape_arc, "arc", 255, 250)

drawn_turtles.append(drawer)

# Main loop for placing text
running = True
while running:
    if usertext:  # Checks if usertext is not empty
        pen_x = int(screen.textinput("Writing...", "what x position do you want for this line"))
        pen_y = int(screen.textinput("Writing...", "what y position do you want for this line "))   
        tutel.penup()
        tutel.goto(pen_x, pen_y)
        tutel.write(usertext, font=("Calibri", 24, "normal"))
        tutel.pendown()
        drawn_turtles.append(tutel) 
        usertext = ""  # Clear usertext after writing

    screen.update()
    screen.listen()

screen.mainloop()
