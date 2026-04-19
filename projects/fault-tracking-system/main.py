# Veritabanımız
arizalar = [
    {"id": 101, "birim": "Savcılık", "sorun": "Yazıcı çalışmıyor", "durum": "Bekliyor"},
    {"id": 102, "birim": "Hâkim Odası", "sorun": "İnternet yok", "durum": "Çözüldü"},
    {"id": 103, "birim": "Ön Büro", "sorun": "Ekran kırık", "durum": "Bekliyor"},
    {"id": 104, "birim": "İcra Dairesi", "sorun": "Toner bitti", "durum": "Bekliyor"},
]

# --- GÖREV 1: BEKLEYEN İŞLER ---
print("--- 🔧 GÖREV 1: BEKLEYEN İŞLER ---")
for kayit in arizalar:
    # try-except harika bir güvenlik önlemi.
    try:
        if kayit["durum"] == "Bekliyor":
            print(f"Acil: {kayit['birim']} - {kayit['sorun']}")
    except KeyError:
        print("Hata: Veri bozuk.")

# --- GÖREV 2: İSTATİSTİK ---
print("\n--- GÖREV 2: İSTATİSTİK ---")

cozulen_sayaci = 0
toplam_ariza = len(arizalar)

for kayit in arizalar:
    if kayit["durum"] == "Çözüldü":
        cozulen_sayaci += 1

# Döngü bitti, şimdi rapor zamanı
print(f"Toplam Arıza: {toplam_ariza}")
print(f"Çözülen Arıza: {cozulen_sayaci}")
print(f"Bekleyen Arıza: {toplam_ariza - cozulen_sayaci}")

# --- GÖREV 3: ARIZA GİDERME (GÜNCELLEME) ---
print("\n--- GÖREV 3: ARIZA GİDERME ---")

try:
    girilen_id = int(input("Çözülen arıza ID'sini girin (Örn: 101): "))

    bulundu_mu = False  # Kontrol mekanizması

    for kayit in arizalar:
        if kayit["id"] == girilen_id:
            
            kayit["durum"] = "Çözüldü"

            print(f"✅ İŞLEM BAŞARILI: {kayit['birim']} arızası giderildi.")
            print(f"Güncel Kayıt: {kayit}")

            bulundu_mu = True
            break  # Aradığımızı bulduk, döngüyü boşuna döndürmeye gerek yok (Performans!)

    if not bulundu_mu:
        print("❌ Hata: Bu ID'ye sahip bir kayıt bulunamadı.")

except ValueError:
    print("⚠️ Lütfen geçerli bir sayı giriniz!")
