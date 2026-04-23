import os
import django
import socket

# 1. Django ortamını dışarıdan çalışacak şekilde ayarlıyoruz (Sihir burada)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'security_arsenal.settings')
django.setup()

# 2. Artık modellerimizi sanki Django içindeymişiz gibi import edebiliriz!
from targets.models import Target

def scan_ports(ip, ports):
    """Verilen IP'deki portları tarar ve açık olanların listesini döner."""
    open_ports = []
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5) # Yarım saniye bekle
        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(str(port))
        sock.close()
    return open_ports

def main():
    print("🛡️ Red Team Scanner Başlatılıyor...")
    
    target_ip = "127.0.0.1"  # Test için kendi makinemizi (localhost) tarayalım
    ports_to_scan = [80, 443, 3306, 5432, 8000] # 8000'i de koyduk ki Django'yu yakalasın :)

    print(f"[*] Hedef taranıyor: {target_ip}")
    found_ports = scan_ports(target_ip, ports_to_scan)

    if found_ports:
        ports_str = ", ".join(found_ports)
        print(f"[+] Açık portlar tespit edildi: {ports_str}")

        # 3. Veritabanına Yazma İşlemi (C# Entity Framework gibi düşün)
        # get_or_create metodu IP varsa getirir, yoksa yeni oluşturur (mükerrer kaydı önler)
        target, created = Target.objects.get_or_create(
            ip_address=target_ip,
            defaults={'hostname': 'Local Test Machine', 'vulnerability_status': 'Clean'}
        )
        
        # Portları güncelle ve kaydet
        target.open_ports = ports_str
        target.save()
        
        if created:
            print("[+] Yeni hedef veritabanına eklendi!")
        else:
            print("[+] Mevcut hedefin port bilgileri güncellendi!")
    else:
        print("[-] Açık port bulunamadı.")

if __name__ == "__main__":
    main()