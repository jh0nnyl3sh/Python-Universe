import os
import json
import logging

class AuditAnalyzer:
    def __init__(self, target_dir, report_file, log_file):
        self.target_dir = target_dir
        self.report_file = report_file
        self.log_file = log_file
        
        logging.basicConfig(
            filename=self.log_file,
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        
        self.audit_results = {
            "High_Risk": [],
            "AI_Compliance": [],
            "Standard": [],
            "Error": []
        }

    def _analyze_document(self, file_path):
        try:
            # Türkçe karakter sorunları yaşamamak için encoding='utf-8' ekliyoruz
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read().lower()
                
                # TASK 1: 'Keyword' analizini yap.
                # Eğer 'content' içinde "risk" veya "manipülasyon" varsa "High_Risk" döndür.
                # Eğer "yapay zeka" veya "algoritma" varsa "AI_Compliance" döndür.
                # Hiçbiri yoksa "Standard" döndür.
                
                # BURAYI SEN YAZ
                if "risk" in content or "manipülasyon" in content:
                    return "High_Risk"
                elif "yapay zeka" in content or "algoritma" in content:
                    return "AI_Compliance"
                else:
                    return "Standard"

        except Exception as e:
            logging.error(f"File read error: {file_path} | Details: {e}")
            return "Error"

    def run_audit(self):
        logging.info("--- Audit Process Started ---")
        if not os.path.exists(self.target_dir):
            logging.critical(f"Directory not found: {self.target_dir}")
            return
        
        for filename in os.listdir(self.target_dir):
            if filename.endswith(".txt"):
                full_path = os.path.join(self.target_dir, filename)
                result_category = self._analyze_document(full_path)
                
                # TASK 2: Dönen 'result_category' değerini kullanarak 
                # 'filename' verisini 'self.audit_results' isimli Dictionary içindeki ilgili List'e append() et.
                
                # BURAYI SEN YAZ
                self.audit_results[result_category].append(filename)
                logging.info(f"Processed: {filename} -> {result_category}")

    def export_findings(self):
        try:
            with open(self.report_file, "w", encoding='utf-8') as f:
                json.dump(self.audit_results, f, indent=4, ensure_ascii=False)
            logging.info(f"Audit findings exported to {self.report_file}")
            print(f"SUCCESS: Denetim raporu {self.report_file} olarak kaydedildi.")
        except Exception as e:
            logging.error(f"JSON export failed: {e}")

def main():
    print("Bağımsız Denetim Analizörü başlatılıyor...")
    
    # TASK 3: AuditAnalyzer sınıfından bir 'Instance' üret.
    # target_dir="audit_data", report_file="audit_report.json", log_file="audit.log"
    # Ardından bu nesnenin metodlarını sırasıyla çalıştırarak denetimi tamamla.
    
    # BURAYI SEN YAZ
    analyzer = AuditAnalyzer(target_dir="audit_data", report_file="audit_report.json", log_file="audit.log")
    analyzer.run_audit()
    analyzer.export_findings()

if __name__ == "__main__":
    main()