from passwordlist import passwords
from passwordlist import target_password


for password in passwords:

    if password == target_password:
        print("✅ Sisteme Sızıldı!")
        break
    
    else:
        print(f"❌ Denenen şifre yanlış: {[password]} ")