from fastapi import FastAPI

# Uygulamamızı (instance) oluşturuyoruz
app = FastAPI(title="İlk API Denemesi")

# 1. Endpoint: Ana Sayfa (Root)
# Tarayıcıdan doğrudan adrese girildiğinde burası çalışır.
@app.get("/")
def read_root():
    return {
        "status": "success",
        "message": "FastAPI sunucusu basariyla calisiyor!"
    }

# 2. Endpoint: Parametre alan bir URL
# URL sonuna yazilan ID numarasini yakalar ve JSON olarak dondurur.
@app.get("/dosya/{dosya_id}")
def read_item(dosya_id: int):
    return {
        "dosya_numarasi": dosya_id,
        "islem_durumu": "Beklemede",
        "aciklama": f"{dosya_id} numarali dosya kuyruga alindi."
    }