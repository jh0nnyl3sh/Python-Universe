import os
import json

TARGET_DIRECTORY = "raw_data"
REPORT_FILE = "classification_report.json"

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
    print("--- Day 97: Data Export System Started --- \n")

    classified_data = {
        "Judge": [],
        "Prosecutor": [],
        "Unknown": [],
        "Error": []
    }
    
    # Verileri okuyup gruplandırmak
    for filename in os.listdir(TARGET_DIRECTORY):
        if filename.endswith(".txt"):
            full_path = os.path.join(TARGET_DIRECTORY, filename)
            entity_type = classify_entity(full_path)
            classified_data[entity_type].append(filename)
            
    print("Data grouped in memory. Exporting to JSON...")
    # Sonuçları JSON formatında kaydetmek
    
    with open(REPORT_FILE, "w") as f:
        json.dump(classified_data, f, indent=4)
        print(f"Classification report saved to  {REPORT_FILE}")
        
if __name__ == "__main__":
    main()