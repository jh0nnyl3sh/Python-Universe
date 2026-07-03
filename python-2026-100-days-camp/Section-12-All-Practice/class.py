# Class Örnekleri

class Car:
    
    def __init__(self, marka, model, yakit_seviyesi):
        self.marka = marka
        self.model = model
        self.yakit_seviyesi = yakit_seviyesi
        
        
    def sur(self):
        if self.yakit_seviyesi < 10:
            print("Yakıtınız bitti, lütfen benzin alın!")
            return False # Yakıt bittiyse False dön
        else:
            print(f"Araba sürülüyor... Kalan yakıt: {self.yakit_seviyesi}")
            self.yakit_seviyesi -= 10
            return True # Yakıt yeterliyse True dön
            
        
# araba1 nesnesi oluşturuluyor.
araba1 = Car("BMW", "X5", 100)


# Döngü, sur() method'u True döndürdüğü sürece devam eder.
while araba1.sur():
    pass # Döngüde başka bir işlem yapmıyoruz, sadece sur() method'unu çalıştır.


    