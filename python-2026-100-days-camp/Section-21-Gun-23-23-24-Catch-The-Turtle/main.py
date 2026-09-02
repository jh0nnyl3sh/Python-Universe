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
t.screen.bgcolor("lightblue")
t.speed()






# onclick fonkisyonu ile turtle skor artıyor
SCORE = 0

def increase_score(x, y):
    global SCORE
    SCORE += 1
    score_board.clear()
    score_board.write("Score: {}".format(SCORE), align="center", font=("Courier", 24, "normal"))

increase_score(0, 0)
t.onclick(increase_score)



TIME_LEFT = 20
# timer fonkisyonu ile 20 saniye boyunca geri sayım yapacak
def countdown_timer():
    global TIME_LEFT
    if TIME_LEFT > 0:
        countdown.clear()
        countdown.write("Time: {}".format(TIME_LEFT), align="center", font=("Courier", 24, "normal"))
        TIME_LEFT -= 1
        turtle.ontimer(countdown_timer, 1000)
    else:
        countdown.clear()
        countdown.write("Time's up!", align="center", font=("Courier", 24, "normal"))
        t.hideturtle()  # kaplumbağayı gizle
        turtle.bye()  # pencereyi kapat

countdown_timer()




# Teleport fonkisyonu ile kaplumbağanın yeri belirlenen sürede sürekli değişecek
################################
tp = t.pos()
tp

for i in range(50):
    x = randint(-200, 200)
    y = randint(-200, 200)
    t.teleport(x, y)
    t.pos()


#################################

turtle.done()



# şekli kaplumbağa yap -> YAPILDI
# kalemi kaldır -> YAPILDI
# gerisayım koy
# skor tablosu koy -> Yapıldı
# kablumbağanın yeri belirnen sürede sürekli değişecek -> teleport fonksiyonu ile
# kaplumbağaya tıklayınca skor artacak -> onclick fonksiyonu ile