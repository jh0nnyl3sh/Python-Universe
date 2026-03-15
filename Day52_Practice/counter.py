import csv

# file counter
open_count = 0
closed_count = 0


with open("court_files.csv", mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        status = row["Status"].strip().lower()
       
        if status == "open":
            open_count += 1
        elif status == "closed": 
            closed_count += 1
        else:
            print(f"❌ Unknown status found! 🔍 File No: {row['File_No']} and Status: {row['Status']}")
            
           
print(f"📊 Total Open Files : {open_count} and Total Closed Files : {closed_count}")
