from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="AI Microservice API")

# 1. ADIM: Pydantic.Model (Veri Şablonu)
class DosyaTalebi(BaseModel):
    dosya_no: int
    konu: str
    sayfa_sayisi: int
    gizlilik_derecesi: bool = False
    

@app.get("/")
def ana_sayfa():
    return {"mesaj": "Sistem aktif. API ayakta."}


# 2. ADIM: POST Endpoint'i
@app.post("/dosya-analiz")
def analiz_baslat(talep: DosyaTalebi):
    # Pydantic veriyi doğruladıysa kod buraya ulaşır.
    return {
        "mesaj": "Dosya basariyla kabul edildi.",
        "alinan_dosya_no": talep.dosya_no,
        "islem": f"'{talep.konu}' konulu, {talep.sayfa_sayisi} sayfalik dosyanin yapay zeka analizi siraya alindi."
    }

    
