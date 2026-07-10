# YouTube Downloader

Python ile geliştirilmiş, CLI (Command Line Interface) üzerinden çalışan basit ve etkili bir YouTube video indirme aracıdır.

Bu `script`, YouTube'un sürekli değişen `API` ve `endpoint` yapıları nedeniyle orijinal `pytube` kütüphanesinde yaşanan `HTTP Error 410: Gone` hatalarını aşmak için modern ve güncel `package`'ler kullanılarak tasarlanmıştır.

## Özellikler (Features)

*   YouTube videolarını hızlı bir şekilde lokal ortama `download` etme.
*   En düşük veya istenilen çözünürlükte medya formatı seçimi.
*   `pytubefix` (hızlı çözüm) ve `yt-dlp` (endüstri standardı) entegrasyonu.

## Gereksinimler (Prerequisites)

*   Python 3.x
*   `pip` (Python Package Installer)
*   Tavsiye edilen: İzole bir çalışma ortamı için `virtual environment` (venv, conda vb.)

## Kurulum (Installation)

1. Projeyi lokal bilgisayarınıza `clone`'layın veya indirin:
   ```bash
   git clone <repository-url>
   cd YouTube-Downloader
   ```

2. Gerekli `dependency`'leri kurun. Hangi yapıyı kullanmak istediğinize bağlı olarak aşağıdaki `package`'lerden birini seçebilirsiniz:

   **yt-dlp (Önerilen - Daha Stabil):**
   ```bash
   pip install yt-dlp
   ```

   **pytubefix (pytube alternatifi):**
   ```bash
   pip install pytubefix
   ```

## Kullanım (Usage)

Terminal üzerinden `script`'i çalıştırın ve indirmek istediğiniz videonun URL'sini girin:

```bash
python youtubedownloader.py
```

### Örnek Kod Yapısı (yt-dlp ile)
```python
import yt_dlp

url = input("Enter the YouTube video URL: ")

ydl_opts = {
    'format': 'worst', 
    'outtmpl': '%(title)s.%(ext)s'
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
```

## Katkıda Bulunma (Contributing)

Geliştirmelere açığız. Eğer projeye katkıda bulunmak isterseniz:
1. Bu `repository`'i `fork`'layın.
2. Yeni bir `branch` oluşturun (`git checkout -b feature/YeniOzellik`).
3. Değişikliklerinizi `commit`'leyin (`git commit -m 'Yeni bir özellik eklendi'`).
4. `branch`'inize `push` yapın (`git push origin feature/YeniOzellik`).
5. Bir `Pull Request` (PR) oluşturun.
