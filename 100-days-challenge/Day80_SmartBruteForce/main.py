import time
from passwordlist import passwords, target_password

guvenlik_sayaci = 0

# Listenin içindeki şifreleri sıra ile alıyoruz.
for password in passwords:

    # 1. ADIM: Önce ban yiyip yemediğimizi kontrol edelim.
    if guvenlik_sayaci == 3:
        print("⚠️ WAF Koruması tetiklendi! Ban yememek için 3 saniye bekliyoruz.")
        time.sleep(3)
        guvenlik_sayaci = 0 # Sayacı sıfırladı, sistem temizlendi.
        
    # 2. ADIM: şifreyi deneyebiliriz.
    if password == target_password:
        print(f"✅ Sisteme Sızıldı! Şifre bulundu : {password}")
        break # Hedefe ulaştık, tüm aramayaı durdur.
    
    else:
        print(f"❌ Deneme şifre yanlış: {password}")
        guvenlik_sayaci += 1 # Şifre yanlışsa sayacı 1 arttır ve for döngüsü bir sonraki şifreyle devam etsin.
    