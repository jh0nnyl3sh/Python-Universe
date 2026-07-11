# Image Background Remover

Bu proje, `rembg`, `numpy` ve `Pillow` kullanarak resimlerin arka planını (background) silmeye yarayan basit bir Python `script`'idir.

## Gereksinimler

*   Python 3.x
*   `pip` (Python Package Installer)

## Kurulum

1. Bu `repository`'yi lokal bilgisayarınıza indirin veya clone'layın.
2. (Opsiyonel ama tavsiye edilen) Bir `virtual environment` oluşturun ve aktif edin.
3. Gerekli kütüphaneleri (library) kurun. Özellikle Mac ve genel CPU kullanıcıları için `onnxruntime` `backend`'ini içeren CPU versiyonu kurulmalıdır:

```bash
pip install "rembg[cpu]" Pillow numpy
```

## Kullanım

1. Arka planını kaldırmak istediğiniz görüntüyü (image) proje dizinine ekleyin (Örn: `kovboy.jpg`).
2. Python `script`'i içindeki dosya isimlerini kendi `image` dosyanıza göre güncelleyin.
3. Terminal üzerinden `script`'i çalıştırın:

```bash
python removebg.py
```

Çıktı (output), arka planı transparan olacak şekilde bir PNG dosyası olarak kaydedilecektir (Örn: `kovboy_no_bg.png`).

## Kod Yapısı

```python
import rembg
import numpy as np
from PIL import Image

# Load the input image
input_image = Image.open("kovboy.jpg")

# Convert the input image to a numpy array
input_array = np.array(input_image)

# Apply background removal using rembg
output_array = rembg.remove(input_array)

# Create a PIL Image from the output array
output_image = Image.fromarray(output_array)

# Save the output image
output_image.save("kovboy_no_bg.png")
```