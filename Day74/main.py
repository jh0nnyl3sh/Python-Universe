import socket
import sys
from datetime import datetime

class ServiceMonitor:
    
    # 2- INIT
    def __init__(self, target_ip):
       self.target_ip = target_ip
       # Dictionary başına self. ekledik ki diğer methodlardan ulaşabilelim
       self.status_log = {} 
       
    # 3- CHECK SERVICES
    def check_services(self, port_list):
        print(f"\n[*] {self.target_ip} hedefi için servis izleme başlatılıyor...")

        for port in port_list:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(2)
        
            # try bloğunu for döngüsünün İÇİNE aldık
            try:
                # Sadece bağlanmayı deniyoruz, banner okumaya (recv) gerek yok
                sock.connect((self.target_ip, port))
                print(f"🟢 Port {port} [UP] - Servis Ayakta!")
                self.status_log[port] = "UP"
                
            except ConnectionRefusedError:
                print(f"🔴 Port {port} [DOWN] - Bağlantı Reddedildi (Kapalı).")
                self.status_log[port] = "DOWN"
                
            except Exception as e:
                print(f"🔴 Port {port} [DOWN] - Hata veya Timeout ({e})")
                self.status_log[port] = "DOWN"
                
            finally:
                sock.close()
            
    # 4- LOG RESULTS
    def log_results(self, filename):
        # Eski kayıtlar silinmesin diye "w" (write) yerine "a" (append/ekleme) modunda açıyoruz
        with open(filename, "a", encoding="utf-8") as file:
            
            # Kayıtlara anlık tarih ve saat ekliyoruz
            zaman = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(f"\n--- Tarama Zamanı: {zaman} ---\n")

            # Sözlükteki (dictionary) port ve durum verilerini txt'ye yazıyoruz
            for port, durum in self.status_log.items():
                file.write(f"Port {port} -> Durum: {durum}\n")
                
        print(f"\n[+] Sonuçlar başarıyla {filename} dosyasına eklendi.")

# Scripti test etme (Yine yasal test ortamımız scanme.nmap.org kullanıyoruz)
monitor = ServiceMonitor("scanme.nmap.org")
monitor.check_services([22, 80, 443, 8080])
monitor.log_results("uptime_report.txt")