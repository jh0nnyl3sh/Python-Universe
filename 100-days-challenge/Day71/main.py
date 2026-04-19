import socket

class RealNetworkScanner:
    
    def __init__(self, target_ip):
        self.target_ip = target_ip
        self.open_ports = []

        
    def scan_ports(self, port_list):
        print(f"[*] {self.target_ip} üzerinde tarama başlatılıyor...\n")    

        for port in port_list:
            # Yeni bir socket object oluşturuyoruz (Ipv4 ve TCP için)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            # Bağlantı denemesi için timeout süresi belirtiyoruz
            sock.settimeout(1) # -> 1 saniye

            # connect_ex methodu başarılı olursa 0, hata alırsan error code döner
            result = sock.connect_ex((self.target_ip, port))

            if result == 0:
                print(f"🔓 Port {port} AÇIK!")
                self.open_ports.append(port)

            else:
                print(f"🔒 Port {port} KAPALI.")

            # İşlem bitince socket'i kapatıyoruz
            sock.close()

    
    def generate_report(self):
        print(f"\n[+] Tarama Tamamlandı.")
        print(f"\n[+] Bulunan Açık Portlar: {self.open_ports}")
        
# Test için kendi bilgisayarını (localhost) tarayabilirsin
scanner = RealNetworkScanner("127.0.0.1")
scanner.scan_ports([21, 22, 80, 443, 3306, 8080])
scanner.generate_report()
