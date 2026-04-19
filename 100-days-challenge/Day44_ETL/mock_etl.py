import pandas as pd
from pathlib import Path
import re

# 1. EXTRACT : Sahte (Mock) Veritabanımız

raw_data = [
    {"Dosya_No": "2026/101", "Taraf" : "Ahmet Yılmaz", "Adres": "Atatürk Mah. No:12 Kadikoy/ISTANBUL"},
    {"Dosya_No": "2026/102", "Taraf": "Ayse Demir", "Adres": "Cumhuriyet Cad. Besiktas/ISTANBUL"},
    {"Dosya_No": "2026/103", "Taraf": "Mehmet Kaya", "Adres": "Kizilay Meydani No:1 Cankaya/ANKARA"},
    {"Dosya_No": "2026/104", "Taraf": "Fatma Sahin", "Adres": "Moda Sahili Kadikoy/ISTANBUL"}
]


class ReportPipline:
    def __init__(self, veri_listesi):
        # Veriyi pandas dataframe objesine çeviriyoruz
        self.df = pd.DataFrame(veri_listesi)
        # Çıktıların kaydedileceği ana Directory 
        self.ana_klasor = Path("Adliye_Raporlari")
        
    def transform_data(self):
        print("[🚀] Transform (Veri Temizleme) başlatılıyor...")

        # Regex ile Adres sütunundan ilçe ve ili ayıklıyoruz.
        # Formatımız : "İlçe/İl" şeklinde olduğu için '/' karakterinden bölüyoruz.
        # Dünya standardı : Pandas split methodu
        ayrilmis_adres = self.df["Adres"].str.split("/", expand=True)
        
        # DataFrame'e yeni sütunlar ekliyoruz
        self.df["Ilce"] = ayrilmis_adres[0].str.split().str[-1] # İlçe genelde /'den önceki son kelimedir.
        self.df["Il"] = ayrilmis_adres[1].str.split() # /'dan sonraki kelime İl'dir. boşlukları sileriz.
        
        print("[+] Veri normalize edildi, İl ve İlçe sütunları ayrıştırıldı")
        print("-" * 50)
        print(self.df[["Taraf", "Ilce", "Il"]]) # Temizlenmiş halini ekrana bas
        print("-" * 50)
        
    def load_data(self):
        print("\n[📁] Load (Klasörleme ve Excel Export) başlatılıyor...")
        
        self.ana_klasor.mkdir(exist_ok=True)
        
        # DataFrame içindeki her bir satır için döngü kuruyoruz
        for index, row in self.df.iterrows():
            
            # --- MİMARIN DOKUNUŞU (Veri Tipi Temizliği) ---
            # Eğer 'Il' verisi liste olarak geldiyse 0. indeksini al (içindeki yazıyı çıkar)
            # Eğer zaten String ise aynen bırak ve garanti olsun diye str() ile sar.
            il_temiz = str(row["Il"][0]) if isinstance(row["Il"], list) else str(row["Il"])
            ilce_temiz = str(row["Ilce"][0]) if isinstance(row["Ilce"], list) else str(row["Ilce"])
            taraf = str(row["Taraf"])
            
            # 1. Dinamik Directory (Klasör) Yolunu İnşa Et
            # Artık listelerle değil, saf String'lerle Path oluşturuyoruz
            hedef_klasor = self.ana_klasor / il_temiz / ilce_temiz
            
            # 2. Klasörü fiziksel olarak yarat
            hedef_klasor.mkdir(parents=True, exist_ok=True)
            
            # 3. Excel Dosyasının tam yolunu belirle
            excel_yolu = hedef_klasor / f"{taraf.replace(' ', '_')}_{row['Dosya_No'].replace('/', '_')}.xlsx"
            
            # 4. Sadece o satırın verisini Excel'e kaydet
            tek_satirlik_df = pd.DataFrame([row])
            tek_satirlik_df.to_excel(excel_yolu, index=False)
            
            print(f"[+] Kaydedildi: {excel_yolu}")
            
# ---- ORKESTRA ŞEFİ -----
if __name__ == "__main__":
    
    # Object yaratıyoruz
    bot = ReportPipline(raw_data)
    
    # Pipeline Method'larını sırayla ateşle
    bot.transform_data()
    bot.load_data()
    
    print("\n[🎯] Operasyon Başarıyla Tamamlandı. Klasörleri kontrol edebilirsin.")
        