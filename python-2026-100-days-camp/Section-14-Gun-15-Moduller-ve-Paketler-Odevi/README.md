# Section 14: Gün 15: Modüller ve Paketler Ödev

- Bu aşamaya kadar öğrendiğimiz konulardı modüller kullanarak pekiştiriyoruz.

- Bir proje belirleyip, kaynak koduna bakmadan, sadece dökümantasyon ve internet araştırması ile bu projeyi yapmaya çalışacağız.
- Yapay zeka kullanımı yasak !!
- Doğrudan kaynak kod bulmaya çalışmak yasak !!

## Bu Aşamaya Kadar Olan Konular Bu Projede Nasıl Yer Alacak
1. **Modüller ve Paketler :** Proje tek bir `main.py` dosyasından ibaret olmayak. `core/` adında bir paket (klasör) açıp, analiz mantığını orada yazacağım başka bir Python dosyasında tutacak ve ana dosyaya `import` edecek.
2. **OOP ve Sınıflar** : `ThreatAnalyzer` (veya başka bir isimde) isminde bir sınıf oluşturacağız. Bu sınıfın içine verileri alacak bir hazırlık metodu (`__init__`) ve analiz yapacak görev metodları yazacağız.
3. **Veri Tipleri & Index / Koleksiyonlar** : Gelen log verileri muhtemelen uzun metinler (`String`) olacak. Bunları boşluklardan parçalayarak (`split`) listelere dönüştüreceğiz. Hangi index'in IP adresine, hangisinin giriş durumuna (`SUCCESS/FAILED`) denk geldiğini bulup bu veri tiplerini ayrıştıracağız.