import turtle

# turtle shape("turtle")
t = turtle.Turtle()

t.shape("turtle")

def fxn(x, y):
    t.right(90)
    t.forward(100)

t.speed(1)
t.forward(100)
t.onclick(fxn)

turtle.done()