uyap_tebligat_listesi = [
    {"dosya_no": "2026/11", "taraf": "Ali Yılmaz", "durum": "Teslim Edildi"},
    {"dosya_no": "2026/12", "taraf": "Ayşe Demir", "durum": "İade Edildi"},
    {"dosya_no": "2026/13", "taraf": "Mehmet Kaya"},  # KRİTİK HATA: 'durum' key'i hiç yok!
    {"dosya_no": "2026/14", "taraf": "Fatma Şahin", "durum": "Teslim Edildi"},
    {"dosya_no": "2026/15"} # DAHA BÜYÜK HATA: Hem taraf hem durum yok!
]

basarili_teslimat = 0

for tebligat in uyap_tebligat_listesi:
    try:
        if tebligat["durum"] == "Teslim Edildi":
            basarili_teslimat += 1
            
    # Spesifik hatayı (KeyError) yakalıyoruz.
    except KeyError:
        print(f"🚨 [SİSTEM UYARISI] Dosya No: {tebligat['dosya_no']} - Tebligat durum bilgisi eksik, atlanıyor.")

print(f"[GÜN SONU] Toplam Başarılı Teslimat: {basarili_teslimat}")