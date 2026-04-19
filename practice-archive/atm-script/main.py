print("---" * 20)
print("$$$ PYTHON BANKASINA HOŞGELDİNİZ $$$")
bakiye = 1000

while True:
    print("\n" + "---" * 10) # Görsel ayraç
    print(f"Mevcut Bakiye: {bakiye} TL")
    print("1. Para Yatır")
    print("2. Para Çek")
    print("q. Çıkış")

    # Kullanıcıdan input alıyoruz.
    secim = input("İşlem Seçiniz: ").strip().lower()

    if secim == "q":
        print("Çıkış yapılıyor. İyi günler.")
        break

    elif secim == "1": # Para Yatırma
        try:
            yatirilacak_tutar = int(input("Yatırılacak tutar : "))
            if yatirilacak_tutar > 0:
                bakiye += yatirilacak_tutar
                print(f"İşlem Başarılı. Yeni Bakiye: {bakiye} TL")

            else:
                print("Hata. 0 veya negatif tutar yatırılamaz.")
        except ValueError:
            print("Hata. Lütfen sayı girin.")

    elif secim == "2": # Para Çekme
        try:
            cekilecek_tutar = int(input("Çekilecek Tutar : "))

            if cekilecek_tutar > bakiye:
                print(f"Yetersiz Bakiye! En fazla {bakiye} TL çekebilirsinzi.")
            elif cekilecek_tutar <= 0:
                print("Hatalı tutar girdiniz.")
            else:
                bakiye -= cekilecek_tutar
                print(f"Para çekildi. Kalan Bakiye : {bakiye} TL")
        except ValueError:
            print("Hata: Lütfen sayı giriniz.")

    else:
        # 1, 2 veya  q dışında bir şeye basarsa
        print("Hatalı seçim! Lütfen Tekrar Deneyiniz.")

