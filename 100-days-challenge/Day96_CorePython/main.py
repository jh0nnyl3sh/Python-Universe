import os

TARGET_DIRECTORY = "raw_data"

def classify_entity(file_path):
    try:
        with open(file_path, 'r') as f:
            content = f.read().lower()
            if "judge" in content:
                return "Judge"
            elif "prosecutor" in content:
                return "Prosecutor"
            else:
                return "Unknown"
    except Exception as e:
        return "Error"

def main():
    print("--- Day 69: Data Grouping System Started ---\n")
    
    # TASK 1: classified_data adında bir Dictionary oluştur.
    # İçinde "Judge", "Prosecutor", "Unknown" ve "Error" Key'leri olsun.
    # Bu Key'lerin başlangıç Value'ları boş birer List ([]) olmalı.
    
    classified_data = {
        "Judge": [],
        "Prosecutor": [],
        "Unknown": [],
        "Error": []
    }
    
    for filename in os.listdir(TARGET_DIRECTORY):
        if filename.endswith(".txt"):
            full_path = os.path.join(TARGET_DIRECTORY, filename)
            
            # Dosyanın kime ait olduğunu buluyoruz (Örn: "Judge")
            entity_type = classify_entity(full_path)
            
            # TASK 2: Bulunan entity_type'ı Dictionary içindeki doğru Key'i bularak, 
            # o Key'in içindeki List'e append() et.
            
            classified_data[entity_type].append(filename)
    
    # TASK 3: Loop bittikten sonra bu Dictionary içindeki verileri,
    # 'for key, value in classified_data.items():' döngüsü ile düzgünce Console'a yazdır.
    
    for key, value in classified_data.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()