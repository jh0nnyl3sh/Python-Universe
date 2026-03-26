# 1. CLASS : Fabrikanın Şablonu (Kalıp)
class AttackBot:
    
    # INIT (Constructor) : Bot üretim bandından ilk çıktığında ona ne vereceğiz ?
    def __init__(self, bot_name, target_ip):
        # 'self' kelimesi botun aynaya bakıp "BEN" demesidir.
        self.name = bot_name    # Benim adım şu olsun
        self.target = target_ip # Benim hedefim şu olsun
        
        
    # METHOD : Botun yetenekleri (class içindeki fonksiyonlara Method denir)
    def start_attack(self):
        print(f"🚨 [ALERT] {self.name} is initiating on {self.target}...")

        
# -------------------------------------------------------------------

# 2. OBJECTS: Şablondan gerçek ajanlar (Nesneler) üretiyoruz
bot_alpha = AttackBot("Alpha-01", "192.168.1.10")    
bot_beta = AttackBot("Beta-02", "10.0.0.5")

# 3. EXECUTION : Ajanlara emir veriyoruz
bot_alpha.start_attack()
bot_beta.start_attack()