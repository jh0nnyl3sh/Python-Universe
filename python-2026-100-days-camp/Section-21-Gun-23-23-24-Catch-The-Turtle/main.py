import turtle 

screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.title("Catch the Turtle Game")


FONT = ("Arial", 30, "bold")

#score turtle
score_turtle = turtle.Turtle()

def setup_score_turtle():
    score_turtle.hideturtle()
    score_turtle.color("dark blue")
    score_turtle.penup()


    top_hight = screen.window_height() / 2
    y = top_hight * 0.8

    score_turtle.setposition(0, y)
    score_turtle.write(arg="Score: 0", move=False, align="center", font=FONT)


setup_score_turtle()



turtle.mainloop()