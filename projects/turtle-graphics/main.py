import turtle as t

t.speed(0)

t.bgcolor("black")

t.color("aqua")

t.hideturtle()

for i in range(150):
    t.circle(i-1)
    t.left(5)
    
    
    t.color("red")
    for j in range(150):
        t.circle(j-1)
        t.left(5)


t.done()