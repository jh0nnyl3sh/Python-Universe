evrak_havuzu = [
    {"dosya_no": "2026/201", "taraf": "Ahmet Yılmaz", "masraf": 500},
    {"dosya_no": "2026/202", "masraf": 750}, # taraf key'i tamamen eksik
    {"dosya_no": "2026/203", "taraf": "Mehmet Kaya", "masraf": 1200}
]

for evrak in evrak_havuzu:
    try:
        print(f"[BİLGİ] Dosya No: {evrak['dosya_no']} - Taraf: {evrak['taraf']}")
    
    except KeyError:
        print(f"[KRİTİK UYARI] Dosya No: {evrak['dosya_no']} içerisinde 'taraf' verisi eksik! Bu dosya atlandı.")
        
   