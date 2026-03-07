import pandas as pd
import numpy as np

# 1. EXTRACT : Klasik "bozuk" excel'in simülasyonu

kirli_veri = {
    "Sutun_1": ["T.C. ADALET BAKANLIGI", "Rapor Tarihi: 07.03.2026", np.nan, "TC Kimlik", "12345678900", np.nan, "98765432100"],
    "Sutun_2": [np.nan, np.nan, np.nan, "Taraf Adi", " Ahmet Yilmaz ", np.nan, "Ayse Demir "],
    "Sutun_3": [np.nan, "Gizli Kod: 45A", np.nan, "Gereksiz Notlar", "Sisteme girildi", np.nan, "Evrak eksik"],
    "Sutun_4": [np.nan, np.nan, np.nan, "Il/Ilce", "Kadikoy/ISTANBUL", np.nan, " Cankaya/ANKARA "]
}

# DataFrame Object'ini yaratıyoruz
df = pd.DataFrame(kirli_veri)

print("[🚨] RAW DATA (Kirli Veri) : ")
print(df)
print("=" * 60)

""" TEMİZLEME KISMI """
print("\n[🧹] DATA CLEANING (TEMİZLİK) BAŞLIYOR...")

# Adım 1 : Çöp başlıkları kesip atmak (Slicing)
# İlk 3 satır tamamen çöp (Logo, tarih, boşluk). Veri 3. index'ten başlıyor.
# Gerçek Excel okurken bunu pd.read_Excel('dosya.xlsx', skiprows=3) ile de yapabiliriz.
df = df.iloc[3:].reset_index(drop=True)

# Adım 2 : İlk satırı sütun isimleri (Headers) yapmak
# Şu an sütun isimleri "Sutun_1", "Sutun_2". Biz ilk satırı başlık yapacağız.
df.columns = df.iloc[0] # ilk satırı al, başlık yap.
df = df[1:].reset_index(drop=True) # İlk satırı veriden sil

# Adım 3 : İçi tamamen boş olan satırları (NaN) imha etmek (Dropna Method)
# Biri excel'de yanlışlıkla boş satır bırakmış. bunu tek komutla siliyoruz.
# how='all' -> sadece bütün sütunları boşsa sil.
df = df.dropna(how='all')

# Adım 4 : Gereksiz sütunu çöpe atmak (Drop Method)
# "Gereksiz Notlar" sütununa ihtiyacımız yok, Memory'de yer kaplamasın
df = df.drop(columns=["Gereksiz Notlar"])

# Adım 5 : Görünmez boşlukları (Whitespace) tıraşlamak (strip method)
# " Ahmet Yilmaz " gibi hatalı girişleri düzeltiyoruz
df["Taraf Adi"] = df["Taraf Adi"].str.strip()
df["Il/Ilce"] = df["Il/Ilce"].str.strip()

print("[+] VERİ BAŞARIYLA TEMİZLENDİ VE NORMALİZE EDİLDİ")
print("-" * 60)
print(df)
print("-" * 60)