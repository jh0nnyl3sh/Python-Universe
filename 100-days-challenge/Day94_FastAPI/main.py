from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Adliye Dosya Yönetim API - CRUD)")

# Sahte Veritabanımız (Memory)
# Anahtarlar (Key) dosya numarası olacak, Değerler (Value) ise Pydantic objesi.

veritabani = {}

class DosyaTalebi(BaseModel):
    konu: str
    sayfa_sayisi: int
    durum: str = "Beklemede"

    
# ----- CREATE (POST) -----
@app.post("/dosya/{dosya_no}")
def dosya_ekle(dosya_no: int, talep: DosyaTalebi):
    if dosya_no in veritabani:
        raise HTTPException(status_code=400, detail="Bu dosya numarasi zaten kayitli.")
    veritabani[dosya_no] = talep
    return {"mesaj": "Dosya basariyla eklendi.", "dosya": veritabani[dosya_no]}


# ----- READ (GET) -----
@app.get("/dosya/{dosya_no}")
def dosya_getir(dosya_no: int):
    if dosya_no not in veritabani:
        raise HTTPException(status_code=404, detail="Dosya bulunamadi.")
    return veritabani[dosya_no]


# ----- UPDATE (PUT) -----
@app.put("/dosya/{dosya_no}")
def dosya_guncelle(dosya_no: int, talep:DosyaTalebi):
    if dosya_no not in veritabani:
        raise HTTPException(status_code=404, detail="Dosya bulunamadi")
    veritabani[dosya_no] = talep
    return {"mesaj": "Dosya basariyla guncellendi.", "dosya": veritabani[dosya_no]}


# ----- DELETE (DELETE) -----
@app.delete("/dosya/{dosya_no}")
def dosya_sil(dosya_no: int):
    if dosya_no not in veritabani:
        raise HTTPException(status_code=404, detail="Dosya bulunamadi.")
    veritabani.pop(dosya_no)
    return {"mesaj": "Dosya basariyla silindi."}