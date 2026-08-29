import turtle

def fxn(x, y):
    turtle.right(90)
    turtle.forward(100)

turtle.speed(1)
turtle.forward(100)
turtle.onclick(fxn)
turtle.done()