import turtle as tu

# Assuming you have a custom module named shapes with a function polygon
import shapes as sh

screen = tu.Screen()
screen.screensize(500, 500)
screen.title('Draw_v2')

bob = tu.Turtle()

# Draw a polygon with side length 50 and 3 sides
sh.polygon(50, 3, bob)

# Start the main loop
screen.mainloop()
