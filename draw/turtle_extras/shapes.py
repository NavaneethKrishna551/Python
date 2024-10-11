import turtle as tu
import math

def polygon(t, length, sides):
    angle = 360 / sides  # Calculate angle per turn (corrected)

    for i in range(sides):
        t.fd(length)  # Move forward by length
        t.lt(angle) 

def circle(t, r):
    circumference = 2 * math.pi * r
    n = 360
    length = circumference / n
    polygon(t, length,n )

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360

    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n

    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)


def test():
    screen = tu.Screen()
    screen.screensize(500,500)

    tutel = tu.Turtle()

    circle(tutel,169.7)

    while True:
        screen.update()
        screen.mainloop()


