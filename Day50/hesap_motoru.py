import csv

TOTAL_PAYMENT = 0

print("-" * 50)
print("\n🚨 GÜN SONU HESAP MOTORU BAŞLATILIYOR... 🚨\n")
print("-" * 50)

with open("masraflar.csv", mode="r", encoding="utf-8") as dosya:
    okuyucu = csv.DictReader(dosya)
    
    for oku in okuyucu:
        try:
            TOTAL_PAYMENT += int(oku["Masraf_Tutari"])
            
        except ValueError:
            print(f"❌ [HATA] Dosya No: {oku['Dosya_No']} masraf bilgisi hatalı! Atlanıyor...")

print(f"\n📊 Gün Sonu Toplam Masraf : {TOTAL_PAYMENT} TL")