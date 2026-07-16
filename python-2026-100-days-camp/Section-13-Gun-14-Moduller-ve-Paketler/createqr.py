# QR Oluşturucu

import pyqrcode
import png



def create_qr_code(data, filename):
    # QR kodu oluştur
    qr = pyqrcode.create(data)
    
    # QR kodunu PNG formatında kaydet
    qr.png(filename, scale=6)
    
    print(f"QR kodu '{filename}' olarak kaydedildi.")




create_qr_code("https://www.example.com", "example_qr.png")