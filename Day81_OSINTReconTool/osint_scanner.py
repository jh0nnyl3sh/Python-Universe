import time
import requests
import re
from bs4 import BeautifulSoup

class OsintScanner:
    
    def __init__(self, target_url):
        # Hedef siteyi sınıfın hafızasına alıyoruz
        self.target_url = target_url
        
        # KAMUFLAJ: Güvenlik duvarlarını (WAF) atlatmak için sahte tarayıcı kimliği
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
        
    def get_html(self):
        """Hedef siteye bağlanır ve HTML kodunu güvenli bir şekilde çeker."""
        try:
            # ADVANCED: timeout=10 ekleyerek sonsuz bekleyişi (donmayı) engelliyoruz
            response = requests.get(self.target_url, headers=self.headers, timeout=10)
            
            # Eğer site 404 (Bulunamadı) veya 500 (Sunucu Hatası) verirse bunu da yakala
            response.raise_for_status() 
            
            return response.text
            
        except Exception as e:
            # Hatanın ne olduğunu (Timeout mu, Bağlantı kopması mı?) ekrana basıyoruz
            print(f"\n🔴 BAĞLANTI HATASI DETAYI: {e}")
            return None
    
    def extract_links(self, html_content):
        """HTML içindeki tüm linkleri (a href) List Comprehension ile şimşek hızında çeker."""
        soup = BeautifulSoup(html_content, "html.parser")
        
        # ADVANCED PYTHON: 5 satırlık for döngüsü yerine tek satırda filtreleme
        # Mantık: [neyi_istiyorum for eleman in nereden_ariyorum if şartım_nedir]
        return [a.get("href") for a in soup.find_all("a") if a.get("href")]
    
    def extract_emails(self, html_content):
        """HTML içindeki e-posta adreslerini Regex ve Generator (yield) mantığıyla RAM'i yormadan bulur."""
        # İnternetin evrensel e-posta yakalama şablonu
        email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
        
        # ADVANCED PYTHON (Generators): Bulduğumuz verileri listeye doldurup RAM'i şişirmek yerine, 
        # anında dışarı fırlatıyoruz (yield). Motor "tembel" (lazy) modda çalışıyor.
        for match in re.finditer(email_pattern, html_content):
            yield match.group()


# ==========================================
# 🚀 SİSTEM KONTROL PANELİ (EXECUTION)
# ==========================================

# 1. Sınıfı hedef URL ile başlat (Hafızayı kur ve kamuflajı giy)
hedef_site = "http://testphp.vulnweb.com"
tarayici = OsintScanner(hedef_site)

print(f"🌐 Hedefe gidiliyor: {hedef_site} ...\n")

# 2. HTML kodunu çek (get_html motorunu ateşle)
gelen_html = tarayici.get_html()

# Eğer HTML başarıyla geldiyse işlemlere başla
if gelen_html:
    
    # --- BÖLÜM 1: LİNK TARAMASI ---
    print("--- 🔗 LİNK TARAMASI BAŞLIYOR ---")
    bulunan_linkler = tarayici.extract_links(gelen_html)
    print(f"✅ Toplam {len(bulunan_linkler)} adet link bulundu.")
    
    # Çok kalabalık yapmasın diye ilk 5 linki yazdıralım
    for link in bulunan_linkler[:5]:
        print(f"  -> {link}")
    print("  -> ... (devamı var)\n")
    
    
    # --- BÖLÜM 2: E-POSTA TARAMASI ---
    print("--- 🕵️‍♂️ E-POSTA TARAMASI BAŞLIYOR ---")
    
    # Motoru (Generator) rölantide çalıştırıyoruz (Şu an RAM tüketimi sıfır!)
    eposta_motoru = tarayici.extract_emails(gelen_html)
    
    # Motorun içindeki verileri tek tek çekiyoruz (Tembel motoru çalışmaya zorluyoruz)
    email_sayaci = 0
    for email in eposta_motoru:
        print(f"📧 Hedef tespit edildi: {email}")
        email_sayaci += 1
        
    # Eğer döngü hiç çalışmadıysa (sayfada e-posta yoksa)
    if email_sayaci == 0:
        print("⚠️ Bu sayfada açıkta bir e-posta adresi bulunamadı.")
        print("💡 İpucu: Hedef URL'yi bir 'iletişim' veya 'hakkımızda' sayfası olarak değiştirebilirsin.")

else:
    print("❌ Hedefe ulaşılamadı veya HTML çekilemedi.")