class Car:
    
    def __init__(self, marka, model, yakit_seviyesi):
        self.marka = marka
        self.model = model
        self.yakit_seviyesi = yakit_seviyesi
        
    def sur(self):
        # Önce kontrol yapıyoruz.
        if self.yakit_seviyesi < 10:
            print("Yakıtınız bitti, lütfen benzin alın!")
        
        else:
            # yakıt yeterliyse, object'in kendi attribute'unu güncelliyoruz
            self.yakit_seviyesi -= 10
            print(f"Araba sürülüyor... Kalan yakıt: {self.yakit_seviyesi}")