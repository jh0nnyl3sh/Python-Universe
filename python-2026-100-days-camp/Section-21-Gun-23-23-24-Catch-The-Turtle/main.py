

from random import randint, random
import turtle

turtle.shape("turtle")

# Screen setup


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
countdown.color("black")
countdown.penup()
countdown.hideturtle()
countdown.goto(0, 220)
countdown.write("Time: 20", align="center", font=("Courier", 24, "normal"))



# turtle shape("turtle")
t = turtle.Turtle()
screen = turtle.Screen()
screen.setup(width=600, height=600)


# t.shape("turtle")
t.penup()  # kalemi kaldır



# onclick fonkisyonu ile turtle ilerliyor 

"""
def fxn(x, y):
    t.right(90)
    t.forward(100)

t.speed(1)
t.forward(100)
t.onclick(fxn)
"""

# onclick fonkisyonu ile turtle skor artıyor
def increase_score(x, y):
    global score
    score += 1
    score_board.clear()
    score_board.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))



# timer fonkisyonu ile 20 saniye boyunca geri sayım yapacak
def countdown_timer():
    global time_left
    if time_left > 0:
        countdown.clear()
        countdown.write("Time: {}".format(time_left), align="center", font=("Courier", 24, "normal"))
        time_left -= 1
        turtle.ontimer(countdown_timer, 1000)
    else:
        countdown.clear()
        countdown.write("Time's up!", align="center", font=("Courier", 24, "normal"))
        t.hideturtle()  # kaplumbağayı gizle
        turtle.bye()  # pencereyi kapat



# Teleport fonkisyonu ile kaplumbağanın yeri belirlenen sürede sürekli değişecek
################################
tp = turtle.pos()
tp

for i in range(20):
    x = randint(-200, 200)
    y = randint(-200, 200)
    turtle.teleport(x, y)
    turtle.pos()
    turtle.speed(10)

#################################

turtle.done()



# şekli kaplumbağa yap -> YAPILDI
# kalemi kaldır -> YAPILDI
# gerisayım koy
# skor tablosu koy -> 
# kablumbağanın yeri belirnen sürede sürekli değişecek -> teleport fonksiyonu ile
# kaplumbağaya tıklayınca skor artacak -> onclick fonksiyonu ile