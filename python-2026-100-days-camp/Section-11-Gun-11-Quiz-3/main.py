#1) Aşağıdaki kodun çıktısı ne olacaktır?
def toplama(a,b):
    print(a,b)
'''
x = toplama(3,4)
print(x)
'''
'\nx = toplama(3,4)\nprint(x)\n'
# cevap
#2) Aşağıdaki kodun çıktısı ne olacaktır?
def usselIslem(x=5,y=3):
    print(x ** y)
usselIslem(2,4)

# cevap
#3) Aynı fonksiyonu aşağıdaki gibi çağırırsak çıktı ne olur?
usselIslem()

# cevap
#4) Aşağıdaki kodun çıktısı ne olacaktır?
def myLoop(*args):
    for element in args:
        print(element / 2)
myLoop(3,2,1,5,3,4)

# cevap
#5) Aşağıdaki dizide belirtilen rakamları, myFunction fonksiyonuna tabi tutup, yeni bir dizi oluşturunuz
def myFunc(num):
    return num ** 3
myList = [2,3,4,5,6]
# cevap
# cevap
#6) Aşağıdaki string dizisinde, içinde sadece XYZ geçen barkodları gösterecek yeni bir liste oluşturunuz
barkodDizisi = ["ABC231","SA3123XYZ","XYZA123Q","QRE1231KJ","X112QGL"]
# cevap
# cevap
#7) Aşağıdaki kodu okursanız, ornekFonksiyon çalıştırıldığında en altta yazdırılan print size neyi yazdıracaktır?
myVar = "Atil Samancioglu"

def ornekFonksiyon():
    myVar = "Atil"
    
    def digerFonksiyon():
        print(myVar)
    
    digerFonksiyon()
#ornekFonksiyon()
# cevap
#8) Aşağıda yazdırılan sınıfı incelediğinizde kedim.yasiCarp() kodunun çıktısı ne olacaktır?
class Kedi():
        
    def __init__(self,isim,yas=5):
        self.isim = isim
        self.yas = yas
        
    def yasiCarp(self):
        return self.yas * 3
kedim = Kedi("Tonton")
#kedim.yasiCarp()
# cevap
#9) Aşağıdaki kodun çıktısı ne olacaktır?
class Ogrenci():
    
    def __init__(self,isim,sinavNotu):
        self.isim = isim
        self.__sinavNotu = sinavNotu
    
    def notuGoster(self):
        print(f"{self.isim} sınav notu: {self.__sinavNotu}")
ogrenci = Ogrenci("Mehmet",85)
ogrenci.__sinavNotu = 75
#ogrenci.notuGoster()
# cevap
#10) Soyut sınıflar ve methodlar oluşturmamıza olanak tanıyan, kodlarımızı daha planlı şekilde yazmamızı mümkün kılan
# aynı zamanda büyük projelerde bize yapısal olarak fayda sağlayabilecek OOP prensibinin adı nedir?
# cevap