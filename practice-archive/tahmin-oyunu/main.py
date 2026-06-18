tuttugum_sayi = 7
tahmin_sayisi = 0
kac_tahmin_hakki_var = 3
buldum = 0

while tahmin_sayisi < kac_tahmin_hakki_var and buldum == 0:
    tahmin = int(input("1 ile 10 arasında bir sayı tamin ediniz: "))
    if tahmin == tuttugum_sayi:
        print("Tebrikler!")
        buldum = 1
    
    else:
        print(f"Bilemediniz, Kalan tahmin sayısı: {(kac_tahmin_hakki_var - tahmin_sayisi) -1}")
        tahmin_sayisi += 1
        
    