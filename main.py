
# 'veritabani.py' dosyasını buraya çağırıyoruz.

import veritabani
import time

print("--- ENVANTER YÖNETİM SİSTEMİ v3.0 (MODÜLER) ---")
print("Sistem başlatılıyor...")
time.sleep(1.5) # <--- Programı 1.5 saniye uyut (beklet)


# Fonksiyonları artık 'veritabani.' diyerek çağıracağız.
envanter_listesi = veritabani.veri_yukle()
print("✅ Veriler yüklendi!\n")

while True:
    print("\n1. Listele | 2. Ekle | 3. Arızalılar | 4. Çıkış")
    secim = input("Seçim : ")

    if secim == "4":
        print("Çıkılıyor...")
        break

    elif secim == "1":
        print(f"\nToplam {len(envanter_listesi)} cihaz var.")
        for cihaz in envanter_listesi:
            print(f"- {cihaz['ad']} ({cihaz['marka']})")

    elif secim == "2":
        ad = input("Ad : ")
        marka = input("Marka : ")
        durum = input("Durum : ")

        # DİKKAT : Fonksiyonu kendi dosyamızdan değil, modülden çağırıyoruz.
        veritabani.cihaz_ekle(envanter_listesi, ad, marka, durum)
        print("✅ Kaydedildi.")

    elif secim == "3":
        #Yine modülden çağırıyoruz
        arizali = veritabani.arizali_olanlari_getir(envanter_listesi)
        print("\n🚨 ARIZALI CİHAZLAR : ")
        for a in arizali:
            print(f"❌ {a['ad']} - {a['durum']}")




