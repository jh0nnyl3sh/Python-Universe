# Turtle Kütüphanesi ile bir kare çizme örneği

import turtle

# Ekranı oluştur
wn = turtle.Screen()
wn.bgcolor("lightblue")

# Kareyi çizecek kaplumbağa oluştur
square_turtle = turtle.Turtle()
square_turtle.color("red")
square_turtle.pensize(3)

# Kareyi çizme fonksiyonu
def draw_square(size):
    for _ in range(4):
        square_turtle.forward(size)
        square_turtle.right(90)
        
# Kareyi çiz
draw_square(100)
