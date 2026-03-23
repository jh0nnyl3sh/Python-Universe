# Simple Face Detection System

Bu proje, Python ve OpenCV kullanarak web kamerası üzerinden gerçek zamanlı **Face Detection** (Yüz Tespiti) yapmaktadır. 

## Özellikler
* **Haar Cascade** algoritması kullanılarak optimize edilmiştir.
* `minNeighbors` parametresi ile hatalı tespitler (False Positives) minimize edilmiştir.
* M1/M2/M3 MacBook Air üzerinde yüksek performansla çalışır.

## Kurulum
1. Depoyu klonlayın: `git clone ...`
2. Sanal ortam oluşturun: `python -m venv venv`
3. Bağımlılıkları kurun: `pip install -r requirements.txt`
4. Çalıştırın: `python main.py`