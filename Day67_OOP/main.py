class GhostOperative:
    
    def __init__(self, codename, stealth_level):
        self.codename = codename
        self.stealth_level = stealth_level
        self.is_active = True
        
        
    
    
    def report_status(self):
        if self.is_active == True:
            print(f"Ajan {self.codename} sahada. Gizlilik Seviyesi: {self.stealth_level}/10")
        else:
            print(f"❌ {self.codename} is OFFLINE.")
        
        
    def take_damage(self, damage_amount):
        self.stealth_level -= damage_amount
        if self.stealth_level <= 0:
            self.is_active = False
            print(f"🚨 [CRITICAL] {self.codename} is compromised! Extraction required!")


agent_one = GhostOperative("Spectre", 9)
agent_two = GhostOperative("Phantom", 7)

agent_one.report_status()
agent_one.take_damage(4)
agent_one.take_damage(7)
agent_one.report_status()