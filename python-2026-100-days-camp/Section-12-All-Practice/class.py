# Class Örnekleri

class Car:
    
    def __init__(self, marka, model, yakit_seviyesi):
        self.marka = marka
        self.model = model
        self.yakit_seviyesi = yakit_seviyesi
        
        
    def sur(self):
        if self.yakit_seviyesi < 10:
            print("Yakıtınız bitti, lütfen benzin alın!")