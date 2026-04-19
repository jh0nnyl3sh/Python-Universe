import socket
import requests


# 1. TASLAK (BLUEPRINT)  : Ajanın nasıl davranacağını belirleyen fabrika kalıbı
class ReconBot:
    
    # İNŞAATÇI (Constructor): Ajan ilk yaratıldığında (Canlandığında) ne bilecek?
    # C#'daki constructor mantığıdır. Python'da buna '__init__' denir.
    def __init__(self, hedef_ip, hedef_isim):
        # 'self', ajanın bizzat kendisidir! 
        # (C#'taki 'this' kelimesi)
        self.isim = hedef_isim
        self.hedef = hedef_ip  # Ajanın beynine hedefi hazıyoruz
        self.acik_portlar = [] # Ajanın bulduğu kapıları koyacağı kendi gizli cebi
        
    # YETENEK 1: Tarama Fonksiyonu (Artık buna 'Method' diyoruz)
    def port_tara(self, port_listesi):
        print(f"\n[🚀] {self.isim} uyandı! {self.hedef} için tarama başlatılıyor...")
        print("-" * 45)

        for port in port_listesi:
            ajan_soket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            ajan_soket.settimeout(1)
            
            # Dikkat hedefi dışarıdan parametere almıyoruz.
            # Ajan kendi hafuzasından okuyor. (self.hedef)
            sonuc = ajan_soket.connect_ex((self.hedef, port))
            
            if sonuc == 0:
                print(f"[+] Port {port:<4} : AÇIK")
                self.acik_portlar.append(port) # Bulduğunu kendi cebine at
                
            else:
                print(f"[-] Port {port:<4} : KAPALI")

            ajan_soket.close()
            
    # YETENEK 2: Kenbi cebindeki veriyi toplama
    def rapor_ver(self):
        print("\n" + "=" * 45)
        print(f"📊 {self.hedef} İÇİN İSTİHBARAT RAPORU")
        print("=" * 45)

        if len(self.acik_portlar) > 0:
            print(f"[!] Sızma İçin Potansiyel Kapılar : {self.acik_portlar}")
        else:
            print("[-] Hedef tamamen kapalı, sızma imkansız.")
            
    
    # WEB Tara
    def web_tara(self):
        print(f"\n[🌍] {self.isim} Web Tarama Protokolüne Geçiyor...")
        # Şimdi ajanın cebine bakıyoruz.
        if 80 in self.acik_portlar:

            # 1. URL'yi doğru formatta string olarak inşa et
            hedef_url = f"http://{self.hedef}"
            
            try:
                cevap = requests.get(hedef_url, timeout=5)
                
                if cevap.status_code == 200 : 
                    print(f"✅ Bağlantı başarılı! Web Sunucusu yanıtı : {cevap.status_code} OK")
                    sayfa_icerigi = cevap.text.lower()
                    
            except requests.exceptions.RequestException:
                print(f"[x] HATA  [{self.hedef}] (Bağlantı Kurulamadı)")
            
        else:
            print("[-] Port 80 kapalı olduğu için Web Taraması iptal edildi.")
    
    

# ---- ORKESTRA ŞEFİ (Kullanım Alanı) ----

# Tek hedef
"""
if __name__ == "__main__" : 
    
    # 1. NESNE YARATMA (Object Instantianiton):
    bot1 = ReconBot("scanme.nmap.org")

    # 2. AJANA EMİR VER: Sadece port listesini veriyoruz, hedefi zaten biliyor
    kritik_portlar = [21, 22, 80, 443]
    bot1.port_tara(kritik_portlar)
    
    # 3. RAPOR İSTE: Bot, başka hiçbir yere sormadan kendi cebindeki veriyi bize döküyor
    bot1.rapor_ver()
    
"""

# Çoklu hedef
if __name__ == "__main__":
    
    # 1. Klon : İnternetteki Nmap Sunucusu
    bot1 = ReconBot("scanme.nmap.org", hedef_isim="Scanme Ajanı")

    # 2. Klon : 
    bot2 = ReconBot("testphp.vulnweb.com", hedef_isim="TestPhp Ajanı")
    
    # Taranacak Portlar
    kritik_portlar = [21, 22, 23, 80, 110, 443, 51]
    
    # Klon 1'i göreve yolla
    bot1.port_tara(kritik_portlar)
    bot1.web_tara()
    
    # Klon 2'yi göreve yolla
    bot2.port_tara(kritik_portlar)
    bot2.web_tara()
    
    # Her ikisinden de rapor isteyelim
    bot1.rapor_ver()
    bot2.rapor_ver()