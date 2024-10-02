import turtle as tu
import math


def polygon(side_length, sides, turtle):
    for _ in range(sides):
        turtle.forward(side_length)
        turtle.left(360 / sides)
