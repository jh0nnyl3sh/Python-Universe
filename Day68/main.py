# 1-
class TargetServer:
    
    def __init__(self, ip_address):
        self.ip_address = ip_address
        self.firewall_active = True # -> bunu init içine yazmaya gerke yok. zaten default olarak aktif
        
    def disable_firewall(self):
        self.firewall_active = False
        print(f"🔒 Firewall down on {self.ip_address}")
        


    
# 2-
class ReconBot:
    def __init__(self, bot_name):
        self.bot_name = bot_name
        
    def scan_target(self, target):
        if target.firewall_active == True:
            print(f"🚨 Scan Failed! {self.bot_name} blocked by {target.ip_address} firewall")

        else:
            print(f"🎯 Scan Successful! {self.bot_name} accessed {target.ip_address} data.")

# 3- Execution
server_alpha = TargetServer("192.168.1.50")
bot_omega = ReconBot("Omega-Scanner")

print("Step - 1")
bot_omega.scan_target(server_alpha)
print("Step - 2")
server_alpha.disable_firewall()
print("Step - 3")
bot_omega.scan_target(server_alpha)