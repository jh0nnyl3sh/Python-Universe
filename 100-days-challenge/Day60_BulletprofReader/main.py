import csv

target_file = "hayalet_dosya.csv"

# 1- Function Definition
def secure_file_reader(file_path):
    
    try:
        with open(file_path, mode="r", encoding="utf-8") as file:
            
            reader = csv.DictReader(file)
            
            
            data_list = list(reader)
            return data_list
            
    
    except FileNotFoundError:
        print("❌ [ERROR]: Target file does not exist. Operation aborted safely.")

# Execution        
secure_file_reader(target_file)