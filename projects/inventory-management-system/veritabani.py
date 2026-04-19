import json

def veri_yukle():
    """Veritabanını okur ve listeyi döndürür"""
    try:
        with open("envanter.json", "r", encoding="utf-8") as dosya:
            liste = json.load(dosya)
            return liste
    except FileNotFoundError:
        return []


def cihaz_ekle(mevcut_liste, ad, marka, durum):
    """Lsiteyi ekleme yapar ve dosyaya kaydeder."""
    yeni_cihaz = {
        "ad": ad,
        "marka": marka,
        "durum": durum
    }
    mevcut_liste.append(yeni_cihaz)


# Kayıt İşlemi (Save)
    with open("envanter.json", "w", encoding="utf-8") as dosya:
        json.dump(mevcut_liste, dosya, ensure_ascii=False, indent=4)
    return True #işlem başarılı sinyali


def arizali_olanlari_getir(liste):
    """Arızalıları filtrele"""
    rapor = []
    for cihaz in liste:
        if cihaz["durum"].lower() == "arızalı":
            rapor.append(cihaz)
    return rapor





