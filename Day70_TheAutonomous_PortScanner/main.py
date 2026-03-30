class NetworkScanner:
    
    def __init__(self, target_ip):
        self.target_ip = target_ip
        self.open_ports = []
        
    # Method - 1    
    def scan_ports(self, port_list):
        
        mock_open_ports = [22, 80, 443]
        
        for port in port_list:
            if port in mock_open_ports:
                print(f"🔓 Port {port} AÇIK!")
                self.open_ports.append(port)
            else:
                print(f"🔒 Port {port} KAPALI.")    
    
    # Methot - 2
    def generate_report(self):
        print(f"\n[+] Hedef {self.target_ip} için Tarama Tamamlandı.")
        print(f"\n[+] Bulunan Açık Portlar: {self.open_ports}")

scanner_bot = NetworkScanner("10.0.0.55")
scanner_bot.scan_ports([21, 22, 80, 443, 8080, 3389])
scanner_bot.generate_report()