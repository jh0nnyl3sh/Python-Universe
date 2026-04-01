import socket
import sys

class BannerGrabber:
    
    def __init__(self, target_ip):
        self.target_ip = target_ip
        self.banners = {}

    def grab_banners(self, port_list):
        print(f"\n[*] {self.target_ip} hedefi için Banner Grabbing başlatılıyor...\n")

        
        try:
            for port in port_list:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(2)
                
                # Ağ hatalarını port bazında yakalayacak iş try
                try:
                    sock.connect((self.target_ip, port))

                    try:
                        banner = sock.recv(1024).decode("utf-8").strip()

                        if banner:
                            print(f"🔓 Port {port} AÇIK - Banner: {banner}")
                            self.banners[port] = banner
                        else:
                            print(f"🔒 Port {port} AÇIK - Banner alınamadı (Boş yanıt.)")
                    
                    except socket.timeout:
                        print(f"🔓 Port {port} AÇIK - Ancak banner göndermedi (Timeout).")
                except ConnectionRefusedError:
                    print(f"🔒 Port {port} KAPALI (Connection Refused).")

                except Exception as e:
                    print(f"🔒 Port {port} KAPALI veya ulaşılamıyor ({e}).")

                finally:
                    # İşelm başarılı da olsa hata da verse socket'i mutkala kapatıyoruz
                    sock.close()
        
        except KeyboardInterrupt:
            print(f"\n[!] İşlem kullanıcı tarafından iptal edildi. Kapatılıyor...")
            sys.exit()

            
    def generate_report(self):
        print(f"n[+] Tarama Tamamlandı.")

        if not self.banners:
            print("[-] Hiç banner bulunamadı.")
        else:
            print("[+] Bulunan Banner Bilgileri:")
            
            for port, banner in self.banners.items():
                print(f" - Port {port}   -> {banner}")

                
scanner = BannerGrabber("127.0.0.1")
scanner.grab_banners([21, 22, 23, 25, 80, 110, 139, 443, 445, 3306, 3389])
scanner.generate_report()