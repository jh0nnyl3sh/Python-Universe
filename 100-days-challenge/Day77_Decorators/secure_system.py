import time
from datetime import datetime

# Simüle edilmiş kullanıcı veritabanı
current_user = {
    "username": "JhonyLesh",
    "role": "user"
}

# 1. CUSTOM DECORATOR 
def require_admin(func):
    def wrapper(*args, **kwargs):
        # İşlem saatini al
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        func_name = func.__name__

        # 1. Adım : Yetki Kontrolü
        if current_user.get("role") != "admin":
            error_msg = f"[❌ DENIED] {timestamp} - User: {current_user['username']} tried to access '{func_name}'\n"

            # Log dosyasına yaz
            with open("security_logs.txt", "a", encoding="utf-8") as f:
                f.write(error_msg)

            # Sistemi durdur ve uyarı ver
            print(f"❌ YETKİ REDDEDİLDİ! Bu işlemi yapmak için Admin olmalısınız")
            return None # Fonksiyonu çalıştırmadan iptal et
        
        # 2. Adım : Eğer yetki varsa adıl fonksiyonu çalıştır ve Logla
        success_msg = f"[✅ GRANTED] {timestamp} - User: {current_user['username']} accessed '{func_name}'\n"

        with open("security_logs.txt", "a", encoding="utf-8") as f:
            f.write(success_msg)

        print(f"✅ Erişim Onaylandı. '{func_name}' çalıştırılıyor...\n")

        # Asıl işi yapan fonksiyonu tetikle ve sonucu döndür
        return func(*args, **kwargs)

    return wrapper

# ===============================================
# 2. SİSTEMİN FONKSİYONLARI (Business Logic)
# ===============================================

# Bu fonkisyona herkes erişebilir (Decorator Yok)
def view_public_dashboard():
    print("👉 Herkese açık ana sayfa gönrüntülendi.")

# Bu kritik fonkisyona sadece Admin erişebilir (Decorator VAR)
@require_admin
def delete_database_record(record_id):
    print(f"🗑️ Veritabanındaki {record_id} ID'li kayıt silindi!")

# Başka bir kritik fonksiyon
@require_admin
def view_confidential_audit_report():
    print("📁 Gizli denetim raporu açıldı: Risk seviyesi YÜKSEK.")

# ===============================================
# 3. TEST AŞAMASI
# ===============================================


print(" --- SİSTEM TESTİ BAŞLIYOR ---\n")

view_public_dashboard()
print("-" * 30)

delete_database_record(record_id=404)
print("-" * 30)

view_confidential_audit_report()

print("\n(Güvenlik logları 'security_logs.txt' dosyasına yazıldı.)")