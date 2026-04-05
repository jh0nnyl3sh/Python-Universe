from google import genai

# Kendi API Key'ini buraya yapıştır
API_KEY = "AIzaSyCZwXK1nlQBqiaFQ1KxwZ2hOb9oK23ZJyw"

client = genai.Client(api_key=API_KEY)

print("[*] Hesabınıza tanımlı kullanılabilir modeller listeleniyor...\n")

try:
    # API üzerinden mevcut modelleri (ListModels) çekiyoruz
    for model in client.models.list():
        # Sadece ismi 'gemini' ile başlayan modelleri filtreleyerek ekrana basalım ki kalabalık olmasın
        if "gemini" in model.name.lower():
            print(model.name)
            
except Exception as e:
    print(f"🔴 Beklenmeyen bir hata oluştu: {e}")