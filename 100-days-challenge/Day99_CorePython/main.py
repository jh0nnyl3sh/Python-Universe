import os
import json
import logging

# Kodumuzu bir Class (Sınıf) mimarisi içine alıyoruz.
class DocumentClassifier:
    
    # TASK 1: Constructor (__init__) metodunu tamamla.
    # Dışarıdan gelen parametreleri, 'self' kelimesi ile Class'ın iç değişkenlerine ata.
    def __init__(self, target_dir, report_file, log_file):
        # BURAYI SEN YAZ (Örn: self.target_dir = target_dir)
        self.target_dir = target_dir
        self.report_file = report_file
        self.log_file = log_file

        # Logging konfigürasyonunu Constructor içinde yapıyoruz
        logging.basicConfig(
            filename=self.log_file,
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        
        # Hafızadaki sözlüğümüz artık Class'a ait bir 'Property'
        self.classified_data = {
            "Judge": [],
            "Prosecutor": [],
            "Unknown": [],
            "Error": []
        }

    # Metodlarımızın içine 'self' parametresi eklendi
    def _classify_entity(self, file_path):
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
            logging.error(f"Dosya okuma hatasi: {file_path} | Detay: {e}")
            return "Error"

    def process_directory(self):
        logging.info("--- Processing Started ---")
        if not os.path.exists(self.target_dir):
            logging.critical(f"Kritik Hata: '{self.target_dir}' klasoru bulunamadi!")
            return
        
        for filename in os.listdir(self.target_dir):
            if filename.endswith(".txt"):
                full_path = os.path.join(self.target_dir, filename)
                # Sınıf içindeki metoda ulaşmak için 'self.' kullanıyoruz
                entity_type = self._classify_entity(full_path)
                self.classified_data[entity_type].append(filename)
                logging.info(f"Processed: {filename} -> {entity_type}")

    def export_report(self):
        try:
            with open(self.report_file, "w") as f:
                json.dump(self.classified_data, f, indent=4)
            logging.info(f"Report saved to {self.report_file}")
        except Exception as e:
            logging.error(f"JSON export failed: {e}")


def main():
    print("Sistem baslatiliyor... Log dosyasini kontrol edin.")
    
    # TASK 2: DocumentClassifier sınıfından bir 'Instance' (nesne) üret.
    # Adı 'classifier' olsun. 
    # Parametre olarak "raw_data", "classification_report.json" ve "system.log" ver.
    # Ardından bu nesnenin '.process_directory()' ve '.export_report()' metodlarını sırasıyla çalıştır.
    
    # BURAYI SEN YAZ
    classifier = DocumentClassifier(
        target_dir="raw_data",
        report_file="classification_report.json",
        log_file="system.log"
    )
    classifier.process_directory()
    classifier.export_report()

if __name__ == "__main__":
    main()