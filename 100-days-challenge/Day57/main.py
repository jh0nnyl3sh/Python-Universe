from mock_data import uyap_users

# --- FUNCTION DEFINITION ---
def analyze_access(users):
    # Initialize counters
    admin_count = 0
    standard_count = 0
    
    # Iterate through the dictionary
    for user, status in users.items():
        if status == "Admin":
            admin_count += 1
        elif status == "Standard":
            standard_count += 1
        else:
            # Logical warning for unauthorized/unknown roles
            print(f"⚠️ [WWARNING] {user} has invalid access level: {status}")
            
    # Return the final counts
    return admin_count, standard_count

# --- EXECUTION ---
print("-" * 40)
print("\n--- UYAP Access Analyzer ---")

# Call the function and unpack the result
total_admin, total_standard = analyze_access(uyap_users)

print(f"\n🔒 UYAP Access Report: {total_admin} Admins, {total_standard} Standard Users.")
print("-" * 40)
