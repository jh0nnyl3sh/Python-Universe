# Class Örnekleri

class Car:
    
    def __init__(self, marka, model, yakit_seviyesi):
        self.marka = marka
        self.model = model
        self.yakit_seviyesi = yakit_seviyesi
        
        
    def sur(self):
        if self.yakit_seviyesi < 10:
            print("Yakıtınız bitti, lütfen benzin alın!")
        else:
            print(f"Araba sürülüyor... Kalan yakıt: {self.yakit_seviyesi}")
            self.yakit_seviyesi -= 10
            
            
araba1 = Car("BMW", "X5", 100)



while True:
    
    araba1.sur()
    if araba1.yakit_seviyesi < 10:
        print("Yakıtınız bitti, lütfen benzin alın!")
        break