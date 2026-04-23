# 🛡️ Security Arsenal: Pentest Dashboard & C2 Core

Bu proje, siber güvenlik operasyonları sırasında hedefleri takip etmek, zafiyet durumlarını yönetmek ve otomatik tarama sonuçlarını merkezi bir veritabanında toplamak için geliştirilmiş bir **Command & Control (C2)** çekirdeğidir.

## 🚀 Öne Çıkan Özellikler
- **Django Backend:** Hedeflerin ve sızma durumlarının yönetildiği profesyonel yönetim paneli.
- **Automated Recon:** `scanner.py` betiği ile hedefleri otomatik tarayıp sonuçları doğrudan veritabanına (ORM üzerinden) raporlama.
- **Vulnerability Tracking:** Hedeflerin "Temiz", "Zafiyetli" veya "Ele Geçirildi" olarak anlık takibi.
- **Scalable Architecture:** Bağımsız ajanların (scripts) merkezi sunucuyla konuştuğu modüler yapı.

## 🛠️ Teknik Stack
- **Language:** Python 3.x
- **Framework:** Django (MVT Architecture)
- **Database:** SQLite (Relational Storage)
- **Networking:** Socket programming (Custom Port Scanner)

## 📂 Mimari Yapı
- **targets/:** Hedef modelleri ve admin yönetim mantığı.
- **security_arsenal/:** Ana proje ayarları ve güvenlik konfigürasyonları.
- **scanner.py:** Veritabanı ile entegre çalışan bağımsız ağ tarayıcı betiği.

## ⚡ Hızlı Başlangıç
1. Sanal ortamı aktif edin: `source venv/bin/activate`
2. Gereksinimleri kurun: `pip install django`
3. Veritabanını hazırlayın: `python manage.py migrate`
4. Sunucuyu başlatın: `python manage.py runserver`
5. Otomatik taramayı çalıştırın: `python scanner.py`

## ⚠️ Yasal Uyarı
Bu araç tamamen etik hackerlık ve eğitim amaçlıdır. İzin alınmamış sistemlerde kullanılması yasal sorumluluk doğurabilir.

---
**Developed by [Jh0nnyL3shh](https://github.com/jh0nnyl3sh)**
