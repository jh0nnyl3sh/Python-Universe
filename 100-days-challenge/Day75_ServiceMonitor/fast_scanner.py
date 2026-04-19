# 1- Library

import socket
import sys
import threading
import time

# 2- Class
class FastScanner:
    
    def __init__(self, target_ip):
        self.target_ip = target_ip
        self.open_ports = []

        # Race Condition ı engellemek için kilidi kurduk
        self.lock = threading.Lock()
        
        
    # 3- İşçinin (Thread) yapacağı tekil görev
    def scan_port(self, port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1.5) # Asenkron olduğumu için süre kısalabilir
        
        try:
            result = sock.connect_ex((self.target_ip, port))

            # Eğer port açıksa
            if result == 0:
                # Kilit devreye giriyor. Veri yazılırken diğer thread'ler bekler
                with self.lock:
                    self.open_ports.append(port)
                    print(f"🔓 Port {port} [UP] - AÇIK")
        
        except Exception as e:
            # Multi-threading yapısında ekranın kirlenmemesi için kapalı portları pass geçmek (ekrana basmamak) daha temiz bir pratiktir. 
            pass
        
        finally:
            sock.close()

        
        
                    
    # 4- Orkestra Şefi: Thread'leri yaratır ve yönetir.
    def start_scan(self, port_list):
        print(f"\n[*] {self.target_ip} hedefi için Multi-Threaded tarama başlatılıyor...\n")

        threads = [] # işçileri tutacağımız yer

        # 1. Aşama: Her port için bir işçi (thread) yarat ve sahaya sür
        for port in port_list:
            # target : hangi method çalışacak, args: O methoda hangi parametre gidecek (tuple formatında olmalı, o yüzden virgül var)
            t = threading.Thread(target=self.scan_port, args=(port,))
            threads.append(t)
            t.start()

        # 2. Aşama : Tüm işçilerin dönmesini bekle
        for t in threads:
            t.join()

        print(f"\n[+] Tarama Tamamlandı. Bulunan Açık Portlar: {self.open_ports}")

# ======================================
# TEST AŞAMASI VE SÜRE ÖLÇÜMÜ
# ======================================



target = "scanme.nmap.org"
# Test için geniş bir port listesi hazırlıyoruz (0'dan 100'e kadar)
ports_to_scan = range(1, 101)

scanner = FastScanner(target)

# süreyi başlat
start_time = time.time()

# Taramayı ateşle
scanner.start_scan(ports_to_scan)

# Süreyi bitir ve hesapla
end_time = time.time()
elapsed_time = end_time - start_time

print(f"\n İşlem {elapsed_time:.2} saniyede tamamlandı.")
        
        