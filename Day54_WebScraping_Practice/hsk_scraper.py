import requests
from bs4 import BeautifulSoup

# 1. HEDEF URL (Nereye Bağlanacağız.)
url = "https://www.hsk.gov.tr/Arsiv/duyuru/"

print(f"📡 '{url}' adresine bağlanılıyor...")

# 2. İSTEK GÖNDER 
# Burada get kullanmamızın sebebi, get, post tur.
response = requests.get(url)

# Durum Kodunu Kontrol Et (200 = Başarılı, 400 = Bulunamadı) 
if response.status_code == 200:
    print("✅ Bağlantı Başarılı! Veri alındı.\n")

    # 3. ÇORBAYI HAZIRLA (HTML'i Parçala, anlayabileceğimiz hale getir)
    soup = BeautifulSoup(response.text, "html.parser")
    
    # 4. VERİYİ ÇEK (HTML Madenciliği)
    headlines = soup.find("div", class_="arsivlist").find_all("a")
    
    print("-" * 40)
    print("📰 GÜNCEL İLK 10 HSK DUYURUSU")
    print("-" * 40)

    # İlk 10 duyuruyu çekmek için listeyi [:10] ile sınırlıyoruz.
    for index, headline in enumerate(headlines[:10],1):
        # <a> etiketinin içindeki tüm metni (tarih ve başlık) alıyoruz.
        title_text = headline.get_text(separator=" ", strip=True)
        
        # Linki (href) alıyoruz.
        link = headline.get("href")

        # Eğer link yarım geliyorsa (örneğin /duyuru...) başına site adresini ekliyoruz
        if link and not link.startswith("https"):
            #Bazı linkler // ile başlayabiliyor, onu da kontrol edelim
            if link.startswith("//"):
                full_link = "https:" + link
            else:
                full_link = "https://www.hsk.gov.tr" + link
        else:
            full_link = link
            
        print(f"{index}. {title_text}")
        print(f" 📎 {full_link}\n")
        

else:
    print(f"❌ Hata oluştu! Durum Kodu : {response.status_code}")
    
print("🏁 Tarama Tamamlandı.")

        