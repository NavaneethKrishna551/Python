import turtle as tu
from turtle_extras import shapes as sp


def draw_polygon():
    while True:  # Infinite loop to keep the window open
        try:
            num_sides = int(input("What is the number of sides you want? "))
            if num_sides < 3:
                print("ERROR : 2.1 :  Polygons must have at least 3 sides.")
                continue  # Skip to the next iteration if sides are less than 3
        except ValueError:
            print("ERROR : 2.2 :Please enter a valid integer for number of sides.")
            continue  # Skip to the next iteration on invalid input

        try:
            side_length = int(input("What length do you want? "))
        except ValueError:
            print("ERROR : 3.1 :Please enter a valid integer for side length.")
            continue  # Skip to the next iteration on invalid input

        # Set up the turtle screen and draw the polygon (unchanged)
        screen = tu.Screen()
        screen.screensize(500, 500)
        turt = tu.Turtle()
        sp.polygon(turt, side_length, num_sides)
        screen.update()
        screen.mainloop()
        break  # Exit the loop after successful execution


def draw_circle():
    while True:
        try:
            radius = int(input("What radius do you wnat the radius to be?"))
            break

        except ValueError:
            print("ERROR : 4.1 :Please enter an integer for the radius")
            continue

    screen = tu.Screen()
    screen.screensize(500, 500)
    turt = tu.Turtle()
    sp.circle(turt, radius)
    screen.update()
    screen.mainloop()


def draw_arc():
    while True:
        try:
            angle = int(input("what angle do you want the arc to have? "))


        except ValueError:
            print("ERROR : 5.1 : Please enter a digit for the angle")

        try:
            radius = int(input("what radius do you want the radius to be? "))
            break
        except ValueError:
            print("ERROR: 5.2 : Please enter a digit for the radius")

    screen = tu.Screen()
    turt = tu.Turtle()
    sp.arc(turt, radius, angle)
    screen.update()
    screen.mainloop()


type_of_shape = input("what type of shape do you want polygon(type pg) arc(type arc) circle(cl) \n if you want to test the software , type : test ")

match type_of_shape.lower():
    case "pg":
        draw_polygon()
    case "cl":
        draw_circle()
    case "arc":
        draw_arc()
    case "test":
        sp.test()
    case _:
        print("ERROR : 1 : Enter one from the list")



print("Program finished/Ended successfully")  # Print this message after successful run


