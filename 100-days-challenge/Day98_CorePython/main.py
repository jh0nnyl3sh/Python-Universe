import os
import json
import logging  # YENİ KAHRAMANIMIZ

TARGET_DIRECTORY = "raw_data"
REPORT_FILE = "classification_report.json"

# TASK 1: Logging konfigürasyonunu yap.
# Parametreler: 
# 1. filename='system.log'
# 2. level=logging.INFO
# 3. format='%(asctime)s - %(levelname)s - %(message)s'

logging.basicConfig(
    filename='system.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

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
        # TASK 2: Hatayı sadece return ile yutma, log dosyasına kaydet.
        # İPUCU: logging.error(f"Dosya okuma hatasi: {file_path} | Detay: {e}")
        logging.error(f"Dosya okuma hatasi: {file_path} | Detay: {e}")
        # BURAYI SEN YAZ
        return "Error"

def main():
    # Artık print yok, logluyoruz!
    logging.info("--- Day 98: Data Export System Started ---")
    
    classified_data = {
        "Judge": [],
        "Prosecutor": [],
        "Unknown": [],
        "Error": []
    }
    
    # Klasör yoksa sistemi zarifçe durdur ve logla
    if not os.path.exists(TARGET_DIRECTORY):
        logging.critical(f"Kritik Hata: '{TARGET_DIRECTORY}' klasoru bulunamadi!")
        return
    
    for filename in os.listdir(TARGET_DIRECTORY):
        if filename.endswith(".txt"):
            full_path = os.path.join(TARGET_DIRECTORY, filename)
            entity_type = classify_entity(full_path)
            classified_data[entity_type].append(filename)
            # Her okunan dosyayı INFO olarak logla
            logging.info(f"Processed: {filename} -> {entity_type}")
            
    logging.info("Data grouped in memory. Exporting to JSON...")
    
    try:
        with open(REPORT_FILE, "w") as f:
            json.dump(classified_data, f, indent=4)
        logging.info(f"Classification report saved to {REPORT_FILE}")
    except Exception as e:
        logging.error(f"JSON export failed: {e}")

if __name__ == "__main__":
    main()