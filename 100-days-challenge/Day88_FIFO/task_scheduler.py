# GÖREV 1.1: 'collections' kütüphanesinden 'deque' modülünü import et.

from collections import deque


def gorev_kuyrugu_olustur():
    print("[*] Task Scheduler başlatılıyor...\n")
    
    # GÖREV 1.2: 'deque' kullanarak 'is_kuyrugu' adında boş bir kuyruk oluştur.
    is_kuyrugu = deque()
    
    # GÖREV 1.3: Bu kuyruğa sırasıyla aşağıdaki 3 görevi ekle (Enqueue işlemi).
    # İpucu: Tıpkı listelerde olduğu gibi .append() metodunu kullanacaksın.
    # Görev 1: "Loglari Temizle"
    is_kuyrugu.append("Loglari Temizle")
    # Görev 2: "Veritabanini Yedekle"
    is_kuyrugu.append("Veritabanini Yedekle")
    # Görev 3: "Sunucuyu Yeniden Baslat"
    is_kuyrugu.append("Sunucuyu Yeniden Baslat")
    
    print(f"[+] Güncel Kuyruk Durumu: {is_kuyrugu}")
    return is_kuyrugu

# Test edelim
gorev_kuyrugu_olustur()