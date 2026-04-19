# Python kafe sipariş sistemi
print("---" * 20)
print("$$$ PYTHON KAFEYE HOŞGELDİNİZ")
toplam_hesap = 0
FIYAT_CAY = 20
FIYAT_KAHVE = 50
FIYAT_PASTA = 70

while True:
    print("\n" + "---" * 10 )
    print(f"1. Çay ({FIYAT_CAY} TL)")
    print(f"2. Kahve ({FIYAT_KAHVE} TL)")
    print(f"3. Pasta ({FIYAT_PASTA} TL)")
    print("q. Hesap Öde ve Çık")

    secim = input("Ne Alırdınız? : ").strip().lower()

    if secim == "q":
        print(f"Ödemeniz Gereken Tutar: {toplam_hesap} TL'dir.")
        break

    elif secim == "1":
        toplam_hesap += FIYAT_CAY
        print(f"Çay eklendi. Güncel Hesap: {toplam_hesap} TL'dir.")

    elif secim == "2":
        toplam_hesap += FIYAT_KAHVE
        print(f"Kahve eklendi. Güncel Hesap: {toplam_hesap} TL'dir.")

    elif secim == "3":
        toplam_hesap += FIYAT_PASTA
        print(f"Pasta eklendi. Güncel Hesap: {toplam_hesap} TL'dir.")

    else:
        print("Hatalı tuşlama yaptınız.")
