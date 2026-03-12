uyap_veritabani = {
    "2026/10": "Karara Çıktı",
    "2026/11": "Duruşma Günü Verildi",
    "2026/12": "Bilirkişi İncelemesinde",
    "2026/13": "İstinaf Aşamasında"
}


print("-" * 50)
print("UYAP SORGU MOTORUNA HOŞ GELDİNİZ")
print("-" * 50)


while True:
    print("\nSorgu Yapılabilecek Dosyalar:", list(uyap_veritabani.keys()))

    kullanici_girisi = input("Lütfen dosya no giriniz (Çıkmak için 'q' tuşlayınız): ").strip()

    if kullanici_girisi.lower() == "q":
        print("Sistem kapatılıyor. İyi mesailer...")
        break
    
    try:
        dosya_durumu = uyap_veritabani[kullanici_girisi]
        
        print(f"🚨 {kullanici_girisi} numaralı dosyanın durumu : 🔍 {dosya_durumu}")
        
    except KeyError:
        print("[HATA] Sistemde böyle bir dosya bulunamadı! Lütfen tekrar deneyin.")