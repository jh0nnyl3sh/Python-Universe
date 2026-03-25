# 1- IMPORTS
import requests
import csv

target_url = "https://jsonplaceholder.typicode.com/users"

# 2- FUNCTION DEFINITION
def harvest_users(url):
    
    # 3- EXTRACT
    response = requests.get(url)
    
    if response.status_code == 200:
        raw_users = response.json()
        
        # 4- TRANSFORM
        clean_intel = [] # Boş ana listemiz
        
        for user in raw_users:
            # Döngüdeki o anki 'user' için yeni bir geçici Dictionary oluşturuyoruz
            # Key isimlerini aşağıdaki 'headers' ile BİREBİR aynı yapıyoruz
            temp_dict = {
                "Name": user['name'],
                "Email": user['email'],
                "City": user['address']['city']
            }
            
            # Bu temizlenmiş sözlüğü ana listemize vagon olarak ekliyoruz
            clean_intel.append(temp_dict)

        # 5- LOAD (Sadece bağlantı başarılıysa burası çalışsın diye if bloğunun içine aldık)
        with open("target_intel.csv" , mode="w", newline="", encoding="utf-8") as file:
            headers = ["Name", "Email", "City"]
            
            # Yazıcı motoru
            writer = csv.DictWriter(file, fieldnames=headers)
            
            # Önce en üste başlıkları yazsın
            writer.writeheader()
            
            # Sonra bütün listeyi tek seferde dosyaya bassın
            writer.writerows(clean_intel)
            
        print("✅ Operasyon Başarılı: target_intel.csv dosyası oluşturuldu!")

    else:
        print("🚨 Hedef sunucuya bağlanılamadı")
    
harvest_users(target_url)