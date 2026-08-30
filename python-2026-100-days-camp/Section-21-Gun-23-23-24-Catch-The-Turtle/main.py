

from random import randint, random
import turtle


# Score Board
score_board = turtle.Turtle()
score_board.speed(0)
score_board.color("blue")
score_board.penup()
score_board.hideturtle()
score_board.goto(0, 260)
score_board.write("Score: 0", align="center", font=("Courier", 24, "normal"))


# Countdown
countdown = turtle.Turtle()
countdown.speed(0)
countdown.color("red")
countdown.penup()
countdown.hideturtle()
countdown.goto(0, 220)
countdown.write("Time: 20", align="center", font=("Courier", 24, "normal"))



# turtle shape("turtle")
t = turtle.Turtle()

t.shape("turtle")
t.penup()  # kalemi kaldır



def fxn(x, y):
    t.right(90)
    t.forward(100)

t.speed(1)
t.forward(100)
t.onclick(fxn)


################################


tp = turtle.pos()
tp

for i in range(50):
    x = randint(-300, 100)
    y = randint(-100, 100)
    turtle.teleport(x, y)
    turtle.pos()


#################################

turtle.done()



# şekli kaplumbağa yap -> YAPILDI
# kalemi kaldır -> YAPILDI
# gerisayım koy
# skor tablosu koy -> 
# kablumbağanın yeri belirnen sürede sürekli değişecek -> teleport fonksiyonu ile
# kaplumbağaya tıklayınca skor artacak -> onclick fonksiyonu ile