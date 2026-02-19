import requests
from bs4 import BeautifulSoup
import csv
import time

url = "https://www.adalet.gov.tr/arsiv"  # Ekran görüntüsündeki URL

# 1. KİMLİK GİZLEME (User-Agent Şart!)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

print(f"📡 '{url}' taranıyor... (Kılık değiştirildi 🕵️‍♂️)")
time.sleep(1)

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("✅ Bağlantı Başarılı! HTML analizi başlıyor...\n")
    soup = BeautifulSoup(response.text, "html.parser")
    
    # --- DÜZELTME BURADA ---
    # Div yerine doğrudan 'a' etiketini ve senin bulduğun class'ı hedefliyoruz.
    announcements = soup.find_all("a", class_="ab-announcement")
    
    file_name = "adalet_duyurular.csv"
    
    with open(file_name, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Sıra", "Duyuru Başlığı", "Link"])
        
        count = 0
        print(f"🔍 {len(announcements)} adet potansiyel duyuru bulundu, işleniyor...\n")
        
        for index, item in enumerate(announcements, 1):
            try:
                # 1. Linki al (Zaten 'a' etiketindeyiz, direkt alıyoruz)
                href = item.get("href")
                
                # Link bazen tam, bazen yarım olabilir. Kontrol et.
                if href and not href.startswith("http"):
                    full_link = "https://www.adalet.gov.tr" + href
                else:
                    full_link = href

                # 2. Başlığı al (Senin bulduğun h5 etiketinin içindeki yazı)
                # 'item'ın (a etiketinin) içinde h5 arıyoruz.
                title_tag = item.find("h5")
                
                if title_tag:
                    title_text = title_tag.text.strip()
                else:
                    # Eğer h5 bulamazsa tüm metni alıp temizlesin
                    title_text = item.text.strip()

                # Boş satırları kaydetme
                if title_text:
                    writer.writerow([index, title_text, full_link])
                    # print(f"✅ {index}. {title_text[:40]}...") # Terminali kirletmemek için kapattım
                    count += 1
            
            except Exception as e:
                print(f"⚠️ Satır hatası: {e}")
                continue
                    
    print(f"\n🚀 İŞLEM TAMAM! Toplam {count} duyuru '{file_name}' dosyasına kaydedildi.")
    
else:
    print(f"❌ Siteye erişilemedi. Hata Kodu: {response.status_code}")