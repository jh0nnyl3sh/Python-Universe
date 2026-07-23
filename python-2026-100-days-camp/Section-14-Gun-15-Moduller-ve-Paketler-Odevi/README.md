# Section 14: Gün 15: Modüller ve Paketler Ödev

- Bu aşamaya kadar öğrendiğimiz konulardı modüller kullanarak pekiştiriyoruz.

- Bir proje belirleyip, kaynak koduna bakmadan, sadece dökümantasyon ve internet araştırması ile bu projeyi yapmaya çalışacağız.
- Yapay zeka kullanımı yasak !!
- Doğrudan kaynak kod bulmaya çalışmak yasak !!

## Bu Aşamaya Kadar Olan Konular Bu Projede Nasıl Yer Alacak
1. **Modüller ve Paketler :** Proje tek bir `main.py` dosyasından ibaret olmayak. `core/` adında bir paket (klasör) açıp, analiz mantığını orada yazacağım başka bir Python dosyasında tutacak ve ana dosyaya `import` edecek.
2. **OOP ve Sınıflar** : `ThreatAnalyzer` (veya başka bir isimde) isminde bir sınıf oluşturacağız. Bu sınıfın içine verileri alacak bir hazırlık metodu (`__init__`) ve analiz yapacak görev metodları yazacağız.
3. **Veri Tipleri & Index / Koleksiyonlar** : Gelen log verileri muhtemelen uzun metinler (`String`) olacak. Bunları boşluklardan parçalayarak (`split`) listelere dönüştüreceğiz. Hangi index'in IP adresine, hangisinin giriş durumuna (`SUCCESS/FAILED`) denk geldiğini bulup bu veri tiplerini ayrıştıracağız.
4. **Sözlükler (Dictionary) ve Kümeler (Set)** : Sisteme saldıran benzersiz IP adreslerini bulmak için Kümeleri (`Set`) kullanacağız. Hangi IP'nin kaç kez hatalı deneme yaptığını hafızada tutmak için IP'yi "Anahtar" (Key), başarısız deneme sayısını "Değer" (Value) yapan bir sözlük (Dictionary) inşa edeceğiz.
5. **Kontroller ve Döngüler** : Sİstemin sürekli açık kalmasını ve kullanıcıya bir menü ("1-Logları Oku", "2-Rapor Çıkar", "3-Çıkış") sunmasını sağlamak için while döngüsünü kuracağız.
6. **İç İçe Akışlar (If / For)** : Log listesini bir for döngüsüyle gezecek ve if şartıyla "Eğer durum FAILED ise ve parola deneme sayısı 3'ten fazlaysa bunu şüpheli olarak işaretle" gibi kurallar yazacaksın.