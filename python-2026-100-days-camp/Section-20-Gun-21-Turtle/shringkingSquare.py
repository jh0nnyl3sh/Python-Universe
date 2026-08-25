import turtle   # ilk olarak turtle kütüphanesini içe aktarırız

turtle_screen = turtle.Screen()  # turtle ekranını oluştururuz
turtle_screen.bgcolor("yellow")  # ekranın arka plan rengini sarı
turtle_screen.title("Turtle ile Şekil Çizimi")  # ekranın başlığını belirleriz


turtle_instance = turtle.Turtle() # turtle nesnesini oluştururuz
turtle_instance.color("blue")  # turtle nesnesinin rengini mavi yaparız


def shrinkingSquare(size):


    for i in range(4): # döngünün kaç kere çalışacağını belirtir.
        turtle_instance.forward(size)  # turtle nesnesini 100 birim ileri hareket ettiririz
        turtle_instance.left(90)  # turtle nesnesini 90 derece sola döndür
        size = size - 5


shrinkingSquare(150)  # shrinkingSquare fonksiyonunu çağırırız ve başlangıç boyutunu 100 olarak belirleriz
shrinkingSquare(130)  # shrinkingSquare fonksiyonunu çağırırız ve boyutu 80 olarak belirleriz
shrinkingSquare(110)  # shrinkingSquare fonksiyonunu çağırırız ve boy
shrinkingSquare(90)  # shrinkingSquare fonksiyonunu çağırırız ve boy
shrinkingSquare(80)  # shrinkingSquare fonksiyonunu çağırırız ve boy
shrinkingSquare(60)  # shrinkingSquare fonksiyonunu çağırırız ve boy
shrinkingSquare(40)  # shrinkingSquare fonksiyonunu çağırırız ve boy

turtle.done()  # turtle işlemini bitiririz