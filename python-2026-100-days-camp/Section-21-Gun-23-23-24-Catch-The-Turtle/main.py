import turtle
import random

screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.title("Catch the Turtle Game")
FONT = ("Arial", 30, "bold")
score = 0


#turtle list
turtle_list = []

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


# Grid size

grid_size = 10

def make_turtle(x,y):
    t = turtle.Turtle()
    
    
    def handle_click(x,y):
        global score
        score += 1
        score_turtle.clear()
        score_turtle.write(arg=f"Score: {score}", move=False, align="center", font=FONT)
        #print(x, y)
    
    
    t.onclick(handle_click)
    t.penup()
    t.shape("turtle")
    t.shapesize(2,2)
    t.color("green")
    t.goto(x * grid_size ,y * grid_size)
    turtle_list.append(t)



x_cordinations = [-20, -10, 0, 10, 20]
y_cordinations = [20, 10, 0, -10]


def setup_turtles():
    for x in x_cordinations:
        for y in y_cordinations:
            make_turtle(x, y)




def hide_turtles():
    for t in turtle_list:
        t.hideturtle()




def show_turtles_randomly():
    random.choice(turtle_list).showturtle()
    
    



turtle.tracer(0) # -> Takip etmeyi bırakıyoruz
setup_score_turtle()
setup_turtles()
hide_turtles()
show_turtles_randomly()
turtle.tracer(1) # -> Takip etmeye başlıyoruz

turtle.mainloop()