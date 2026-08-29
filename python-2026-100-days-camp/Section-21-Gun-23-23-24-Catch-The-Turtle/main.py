import turtle # -> Import the turtle module

draw_board = turtle.Screen() # -> Create a screen object for the turtle graphics window
draw_board.bgcolor("lightblue") # -> Set the background color of the turtle graphics window to light blue
draw_board.title("Catch the Turtle Game") # -> Set the title of the turtle graphics window to "Catch the Turtle Game"

turtle_instance = turtle.Turtle() # -> Create a turtle object named turtle_instance

turtle_instance.forward(100) # -> Move the turtle_instance forward by 100 units

turtle.done() # -> Keep the turtle graphics window open until it is manually closed