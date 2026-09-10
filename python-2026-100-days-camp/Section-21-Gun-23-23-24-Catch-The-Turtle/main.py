import turtle 

screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.title("Catch the Turtle Game")


FONT = ("Arial", 30, "bold")

#score turtle
score_turtle = turtle.Turtle()

score_turtle.hideturtle()
score_turtle.color("dark blue")
score_turtle.write(arg="Score: 0", move=False, align="center", font=FONT)





turtle.mainloop()