import requests
import csv 


class DataMiner:
    
    # Attribute
    def __init__(self, target_url):
        self.target_url = target_url
        self.intel_data = [] # -> çekilen veriler burada duracak
    
    # Method - 1
    def fetch_users(self):
        response = requests.get(self.target_url)
        
        if response.status_code == 200:
            raw_users = response.json()            
            
            
            for user in raw_users:
                temp_dict = {
                    "Name": user['name'],
                    "Email": user['email'],
                    "City": user['address']['city'],
                    "Phone": user['phone']
                }
                

                self.intel_data.append(temp_dict)
            print("✅ Veriler başarıyla çekildi ve ajanın hafızasına kaydedildi.\n")

    
    # Method - 2
    def export_to_csv(self, filename):
        
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            headers = ["Name", "Email", "City", "Phone"]
            
            # Yazıcı 
            writer = csv.DictWriter(file, fieldnames=headers)
            
            # önce en üste başlıkları yazsın
            writer.writeheader()
            
            # sonra bütün listeyi tek seferde dosyaya bassın
            writer.writerows(self.intel_data)
        print(f"📁 Dosya başarıyla oluşturuldu: {filename}")
            
miner_bot = DataMiner("https://jsonplaceholder.typicode.com/users")

miner_bot.fetch_users()
        
miner_bot.export_to_csv("target_intel.csv")