import csv

birlesik_veri = {} 

try:
    
    # davalar.csv yi okuyoruz.
    with open("davalar.csv", mode="r", encoding="utf-8") as dosya:
        davalar = csv.DictReader(dosya)
        
        for dava in davalar:
            birlesik_veri[dava["Dosya_No"]] = {"Taraf": dava["Taraf_Adi"], "Masraf": 0}
        
            
            
    # masraflar.csv
    
    with open("masraflar.csv", mode="r", encoding="utf-8") as dosya:
        masraflar = csv.DictReader(dosya)
        
        for masraf in masraflar:
            birlesik_veri[masraf["Dosya_No"]]["Masraf"] = masraf["Masraf_Tutari"]
      
    
except FileNotFoundError:
    print("❌ [KRİTİK HATA] Kaynak dosyalardan biri bulunamadı. Lütfen klasörü kontrol edin!")




print("\n📊 GÜN SONU BİRLEŞTİRİLMİŞ UYAP RAPORU 📊")
print("-" * 50)
for dosya_no, detaylar in birlesik_veri.items():
    print(f"📂 Dosya: {dosya_no} | 👤 Taraf: {detaylar['Taraf']} | 💰 Masraf: {detaylar['Masraf']} TL")
print("-" * 50)