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


grid_size = 10

def make_turtle(x,y):
    t = turtle.Turtle()
    
    t.penup()
    t.shape("turtle")
    t.shapesize(2,2)
    t.color("green")
    t.goto(x * grid_size ,y * grid_size)



make_turtle(-20,20)
make_turtle(-10,20)
make_turtle(0,20)
make_turtle(10,20)
make_turtle(20,20)


make_turtle(-20,10)
make_turtle(-10,10)
make_turtle(0,10)
make_turtle(10,10)
make_turtle(20,10)


make_turtle(-20,0)
make_turtle(-10,0)
make_turtle(0,0)
make_turtle(10,0)
make_turtle(20,0)


make_turtle(-20,-10)
make_turtle(-10,-10)
make_turtle(0,-10)
make_turtle(10,-10)
make_turtle(20,-10)



setup_score_turtle()

turtle.mainloop()