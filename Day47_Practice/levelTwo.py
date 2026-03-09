gelen_dosyalar = [
    {"dosya_no": "2026/101", "sayfa_sayisi": 150},
    {"dosya_no": "2026/102", "sayfa_sayisi": "Yüz Elli"}, # Kirli veri
    {"dosya_no": "2026/103", "sayfa_sayisi": 300}
]


for dosya in gelen_dosyalar:
    try:
        yeni_sayfa = int(dosya["sayfa_sayisi"]) + 50
        
        print(f"[BAŞARILLI] Dosya: {dosya['dosya_no']} - Yeni Sayfa Sayısı: {yeni_sayfa}")
        
    except ValueError:
        print(f"[HATA] Dosya: {dosya['dosya_no']} - Sayfa sayısı hatalı girilmiş. Atlanıyor...")