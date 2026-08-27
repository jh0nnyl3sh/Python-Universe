import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("white")
drawing_board.title("Interactive Drawing Board")

turtle_instance = turtle.Turtle()

# Forward movement = Space 
def turtle_forward():
    turtle_instance.forward(100)

# Left movement = Left    
def turtle_left():
    turtle_instance.left(90)
    
# Right movement = Right
def turtle_right():
    turtle_instance.right(90)

drawing_board.listen()
drawing_board.onkey(fun=turtle_forward, key="space")
drawing_board.onkey(fun=turtle_left, key="Left")
drawing_board.onkey(fun=turtle_right, key="Right")

turtle.mainloop()

