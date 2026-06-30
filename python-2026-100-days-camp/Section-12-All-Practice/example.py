class BudgetTracker:
    
    def __init__(self, hesap_sahibi, bakiye):
        self.hesap_sahibi = hesap_sahibi
        self.bakiye = bakiye
        
    def harcama_yap(self, harcama_tutari):
        # harcamadan önce kontrol yapalım
        if self.bakiye >= harcama_tutari:
            self.bakiye -= harcama_tutari
            print(f"Güncel bakiye : {self.bakiye}")
        else:
            print("Bakiye yetersiz. Lütfen güncel bütçenizi gözden geçirin!")

    # gelir ekleyelim
    def gelir_ekle(self, gelir_tutari):
        self.bakiye += gelir_tutari
        print(f"Güncel bakiye : {self.bakiye}")
        
        

myBudget = BudgetTracker("Jhon", 10000)

while myBudget.bakiye >= 1500:
    print("\n1500 birimlik harcama yapılıyor...")
    myBudget.harcama_yap(1500)
    