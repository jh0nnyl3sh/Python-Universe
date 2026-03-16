import csv

# Open both files at the same time
with open("all_cases.csv", mode="r", encoding="utf-8") as file_in, open("archive_ready.csv", mode="w", encoding="utf-8", newline="") as file_out:
    
    # Set up the reader (it finds headers automatically)
    reader = csv.DictReader(file_in)
    
    # Set up the writer (we MUST tell it the headers)
    writer = csv.DictWriter(file_out, fieldnames=["File_No", "Party_Name", "Status"])
    
    # Write the column titles to the new file first!
    writer.writeheader()
    
    # Loop through the old file and write to the new file
    for row in reader:
        if row["Status"] == "Closed":
            writer.writerow(row)

# Print success message outside the block
print("✅ Archive file created successfully!")