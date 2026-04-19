import csv

# 1. Target File
target_file = "server_logs.csv"

# 2. Function Definition
# İçeri giren parametre ismi 'file_path'
def analyze_security_logs(file_path):
    
    suspicious_count = 0
    
    
    with open(file_path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
    
        
        for row in reader:
            if row["Status_Code"] == "403":
                suspicious_count += 1
                
        return suspicious_count
        
# ------------------------------------------------------------        
# 3. Execution
print("-" * 40)
print("-> Suspicious Activity Monitor <-")


total_suspicious = analyze_security_logs(target_file)

print(f"\n🚨 SECURITY ALERT: {total_suspicious} suspicious (403 Forbidden) attempts detected!")
print("-" * 40)