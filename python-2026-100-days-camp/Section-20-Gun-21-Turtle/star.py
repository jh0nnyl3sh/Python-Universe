# START SHAPING #
import turtle

kose = 0
koseSay = 5
kenarPx = int(input("Kenar uzunluğunu giriniz: "))

yazi_tahtasi = turtle.Screen()
yazi_tahtasi.bgcolor("yellow") # Sayfa arka plan rengi
yazi_tahtasi.title("Turtle ile Şekil Çizimi") # Sayfa başlığı

turtle_ins = turtle.Turtle() # Turtle çalıştır

for i in range(koseSay):
    turtle_ins.forward(kenarPx) # Turtle ileri git
    turtle_ins.left(144) # Yıldızın bir iç açısı 144 derecedir.
    
turtle.done() # Turtle işlemini bitir
