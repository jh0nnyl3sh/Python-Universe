from google import genai
from pydantic import BaseModel, ValidationError

# 1- API Configuration (Kopyaladığın Key'i buraya yapıştır)
API_KEY = "AIzaSyCZwXK1nlQBqiaFQ1KxwZ2hOb9oK23ZJyw"

# Yeni Architecture: Sisteme bağlanmak için Client objesi oluşturuyoruz
client = genai.Client(api_key=API_KEY)

# 2- Pydantic Architecture (Veri şablonumuz)
class AuditData(BaseModel):
    company_name: str
    invoice_amount: float
    risk_level: str
    is_compliant: bool

# 3- Business Logic & Execution
def extract_audit_data(raw_text: str):
    print("[*] LLM modeli analiz ediyor, lütfen bekleyin...\n")
    
    prompt = f"""
    Sen uzman bir bağımsız denetçisin. Aşağıdaki karmaşık metni analiz et ve 
    sadece şu JSON formatında veri döndür (başka hiçbir markdown veya açıklama yazma):
    
    {{
        "company_name": "Şirket Adı",
        "invoice_amount": 0.0,
        "risk_level": "Yüksek/Orta/Düşük",
        "is_compliant": true/false
    }}
    
    Analiz edilecek metin:
    {raw_text}
    """
    
    try:
        # Yeni Library üzerinden Request atıyoruz
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt
        )
        raw_json = response.text.strip().replace('```json', '').replace('```', '')
        
        # 4- Pydantic Validation (Kapı Bekçisi)
        validated_data = AuditData.model_validate_json(raw_json)
        
        print("✅ Data Validation BAŞARILI! Yapılandırılmış Veri:")
        print(f"Şirket: {validated_data.company_name}")
        print(f"Tutar: {validated_data.invoice_amount}")
        print(f"Risk Seviyesi: {validated_data.risk_level}")
        print(f"Uyumlu mu?: {validated_data.is_compliant}")
        
    except ValidationError as e:
        print(f"❌ Pydantic Validation Hatası: LLM istenen Architecture dışına çıktı!\nDetay: {e}")
    except Exception as e:
        print(f"🔴 Beklenmeyen bir hata oluştu: {e}")

# ==========================================
# TEST AŞAMASI
# ==========================================

messy_audit_text = """
Bugün yapılan denetimlerde TechNova Yazılım A.Ş. firmasına ait kayıtlar incelendi. 
Faturanın üzerinde 45000.50 TL yazıyor ancak sistemde farklı bir tutar gördük. 
Ayrıca güvenlik prosedürlerine tam olarak uyulmadığı tespit edildiğinden 
bu durumu oldukça Yüksek riskli olarak raporluyoruz.
"""

# Fonksiyonu çalıştır
extract_audit_data(messy_audit_text)