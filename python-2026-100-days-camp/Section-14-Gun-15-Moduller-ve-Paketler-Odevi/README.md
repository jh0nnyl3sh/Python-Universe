# Section 14: Gün 15: Modüller ve Paketler Ödev

- Bu aşamaya kadar öğrendiğimiz konulardı modüller kullanarak pekiştiriyoruz.

- Bir proje belirleyip, kaynak koduna bakmadan, sadece dökümantasyon ve internet araştırması ile bu projeyi yapmaya çalışacağız.
- Yapay zeka kullanımı yasak !!
- Doğrudan kaynak kod bulmaya çalışmak yasak !!

## Bu Aşamaya Kadar Olan Konular Bu Projede Nasıl Yer Alacak
1. **Modüller ve Paketler :** Proje tek bir `main.py` dosyasından ibaret olmayak. `core/` adında bir paket (klasör) açıp, analiz mantığını orada yazacağım başka bir Python dosyasında tutacak ve ana dosyaya `import` edecek.
2. **OOP ve Sınıflar** : `ThreatAnalyzer` (veya başka bir isimde) isminde bir sınıf oluşturacağız. Bu sınıfın içine verileri alacak bir hazırlık metodu (`__init__`) ve analiz yapacak görev metodları yazacağız.