# 🚀 Day 51: UYAP Data Join & Exception Handling Pipeline

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Data Engineering](https://img.shields.io/badge/Data_Engineering-Pipeline-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)

Bu *Repository*, iki farklı dış veri kaynağından (`.csv`) gelen verileri hafızada çarpıştırarak tek bir anlamlı rapora dönüştüren bir **Data Join** operasyonunu içermektedir. Parçalı verileri otonom olarak birleştirmek için tasarlanmış bir *Proof of Concept* (PoC) çalışmasıdır.

## ✨ Özellikler (*Features*)

* 📂 **File I/O Operasyonları:** Harici dosyaların `csv.DictReader` kullanılarak belleği yormadan güvenle okunması.
* 🔗 **Data Join Mimari:** *Nested Dictionary* (İç içe sözlük) yapısı kullanılarak ortak bir *Key* (`Dosya_No`) üzerinden "Taraf" ve "Masraf" verilerinin havada birleştirilmesi.
* 🛡️ **Defensive Programming:** `FileNotFoundError` kalkanı sayesinde eksik veya silinmiş dosya durumlarında sistemin çökmesini (*Crash*) engelleyen *Exception Handling* mekanizması.
* 🔒 **Data Privacy:** `.gitignore` konfigürasyonu ile hassas verilerin (`*.csv`, `*.xlsx`, `*.pdf`) uzak sunucuya *Push* edilmesinin engellenmesi.

## 🏗️ Proje Yapısı (*Project Structure*)

```text
📁 Day51_DataJoin/
│
├── 📄 veri_birlestirici.py    # Ana Pipeline Scripti
├── 📄 davalar.csv             # UYAP Taraf Verisi (Mock Data)
├── 📄 masraflar.csv           # Vezne Masraf Verisi (Mock Data)
├── 📄 .gitignore              # Veri Güvenliği Kalkanı
└── 📁 venv/                   # Virtual Environment
💻 Çalıştırma (Execution)
Projeyi kendi lokal ortamınızda (Local Environment) çalıştırmak için terminal üzerinden aşağıdaki komutu ateşlemeniz yeterlidir:

Bash
python veri_birlestirici.py
📊 Örnek Çıktı (Console Output)
Plaintext
📊 GÜN SONU BİRLEŞTİRİLMİŞ UYAP RAPORU 📊
--------------------------------------------------
📂 Dosya: 2026/1 | 👤 Taraf: Ahmet Yılmaz | 💰 Masraf: 750 TL
📂 Dosya: 2026/2 | 👤 Taraf: Ayşe Demir | 💰 Masraf: 1500 TL
📂 Dosya: 2026/3 | 👤 Taraf: Mehmet Kaya | 💰 Masraf: 3000 TL
--------------------------------------------------