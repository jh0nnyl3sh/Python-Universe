# 1. Mock Data (Dictionary)
cases = {
    "2026/1": "Open",
    "2026/2": "Open",
    "2026/3": "Closed",
    "2026/4": "Open"
}

print("🔄 System is updating...\n")

# 2. Update a specific case
# We directly access the Key and change its Value. No loop needed!
cases["2026/2"] = "Closed"


# 3. Print the Open Cases
print("📂 CURRENT OPEN CASES:")

# We use .items() to get both the Key (case_no) and Value (status)
for case_no, status in cases.items():
    if status == "Open":
        print(f" - File {case_no} is still Open.")