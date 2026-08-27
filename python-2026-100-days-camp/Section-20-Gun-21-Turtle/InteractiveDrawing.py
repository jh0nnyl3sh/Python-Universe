import turtle

drawing_board = turtle.Screen()
drawing_board.bgcolor("white")
drawing_board.title("Interactive Drawing Board")

turtle_instance = turtle.Turtle()

def turtle_forward():
    turtle_instance.forward(100)
    

drawing_board.listen()
drawing_board.onkey(fun=turtle_forward, key="space")


turtle.mainloop()

