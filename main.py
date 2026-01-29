# Veritabanımız (Bir Liste)
envanter = [
    {
        "id": 101,
        "yer": "Savcılık Kalemi",
        "cihaz": "Laptop",
        "yazilimlar": ["UYAP", "Chrome", "Office"]
    },

    {
        "id": 102,
        "yer": "Hakim Odası",
        "cihaz": "Masaüstü",
        "yazilimlar": ["UYAP", "VPN"]
    }
]

# GÖREV 1: 101 nolu cihazın yerini ekrana yazdır (Savcılık Kalemi).
print(envanter[0]["cihaz"])

# GÖREV 2: 102 nolu cihazın İLK yazılımını ekrana yazdır (UYAP).
print(envanter[1]["yazilimlar"][0])

# GÖREV 3: 101 nolu cihaza "Antivirüs" yazılımını ekle.
# İpucu: Önce listeye ulaş, sonra .append() kullan.
envanter[0]["yazilimlar"].append("Antivirüs")
print(envanter[0]["yazilimlar"][3])

# GÖREV 4 (ZOR): Tüm cihazların yerini ve içindeki yazılım sayısını döngüyle yazdır.
# Örn: Savcılık Kalemi -> 4 yazılım.



for bilgisayar in envanter:
    konum = bilgisayar["yer"]

    yazilim_adedi = len(bilgisayar["yazilimlar"])
    print(f"{konum} -> {yazilim_adedi} adet yazılım yüklü.")










