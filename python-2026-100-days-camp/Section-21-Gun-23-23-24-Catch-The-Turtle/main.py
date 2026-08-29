"""
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
"""


import turtle



x = turtle.Turtle()
y = 5 # Kenar sayısı
z = 50 # kenar uzunluğu
a = 360.0 / y  # daireyi bölen açı
x.shape("turtle") # turtle şekli

for i in range(y):
    x.forward(z) # z kadar ileri git (kenar uzunluğu)
    x.right(a) # a kadar sağa dön (açı)
    
turtle.done()



