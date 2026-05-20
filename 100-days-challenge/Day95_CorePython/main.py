import os

# Verilerin bulunduğu dizin
TARGET_DIRECTORY = "raw_data"

# GÖREV: Bu fonksiyonu tamamla.
def classify_entity(file_path):
    """
    Dosyayı okur, içindeki metne bakar ve 'folder path' e dikkat etmeden 
    sadece 'Keyword' eşleşmesine göre sınıflandırma yapar.
    """
    
    try:
        # 1. 'with open(...)' kullanarak file_path yolundkai dosyayı 'Read' (r) modunda aç.
        # 2. Dosya içeriğini bir 'String' değişkene aktar (örn: content = f.read()).
        # 3. Metni standartlaştırmak için .lower() metodunu kullan (büyük/küçük harf duyarlılığını kaldır)
        # 4. 'Keyword' kontrolü yap:
        #     - Eğer metin içinde "judge" kelimesi geliyorsa "Entity: Judge" döndür.
        #     - Eğer "prosecutor" geçiyorsa "Entity: Prosecutor" döndür.
        #     - İkisi de yoksa "Entity: Unknown" döndür.
        
        with open(file_path, 'r') as f:
            content = f.read().lower()
            if "judge" in content:
                return "Entity: Judge"
            elif "prosecutor" in content:
                return "Entity: Prosecutor"
            else:
                return "Entity: Unknown"
            
    except Exception as e:
        return f"Error reading file: {e}"
    
    
def main():
    print("--- Data Parsing System Started ---\n")
    
    # 'os.listdir' ile dizindeki tüm dosyaları tarıyoruz.
    for filename in os.listdir(TARGET_DIRECTORY):
        if filename.endswith(".txt"):
            full_path = os.path.join(TARGET_DIRECTORY, filename)
            
            entity_type = classify_entity(full_path)
            
            print(f"File: {filename} | Classification: {entity_type}")
            
if __name__ == "__main__":
    main()
    
    