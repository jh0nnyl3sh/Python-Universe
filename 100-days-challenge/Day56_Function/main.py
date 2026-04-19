# 1. MOCK DATA 
court_A_files = {
    "2026/10": "Open",
    "2026/11": "Closed",
    "2026/12": "Open",
    "2026/13": "Pending"
}

# 2. THE FUNCTION
def analyze_cases(case_data):
    # Sayaçlarımız (Local Variables)
    open_count = 0
    closed_count = 0
    
    # Döngümüz başlıyor. .items() ile hem anahtarı (case_no) hem değeri (status) alıyoruz.
    for case_no, status in case_data.items():
        
        # Her bir 'status' kelimesini tek tek kontrol ediyoruz.
        if status == "Open":
            open_count += 1
        elif status == "Closed":
            closed_count += 1
        else:
            # Sadece 'Open' veya 'Closed' olmayanları (Örn: Pending) ekrana basıyoruz.
            print(f"❌ [WARNING] Unknown status for File {case_no}: {status}")
            
    # Döngü tamamen bittikten sonra (hizası dışarıda) sonuçları fırlatıyoruz.
    return open_count, closed_count

# ---------------------------------------------------------
# 4. EXECUTION
print("⚙️ System is analyzing Court A files...\n")

total_open, total_closed = analyze_cases(court_A_files)

print(f"\n📊 Analysis Complete: {total_open} Open Files, {total_closed} Closed Files.")