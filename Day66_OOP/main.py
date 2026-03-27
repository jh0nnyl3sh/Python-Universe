# 1- CLASS ŞABLONU - fabrikanın şablonu
class GhostOperative:
    
    
    # Constructor 
    def __init__(self, codename, stealth_level):
        self.codename = codename
        self.stealth_level = stealth_level
        
        
    # Method : botun yetenekleri (class içindeki fonksiyonlara method denir)
    def report_status(self):
        print(f"Ajan {self.codename} sahada. Gizlilik Seviyesi: {self.stealth_level}/10")

# 2- CLASS OBJECTS: şablondan gerçek nesneler üretiyoruz.

agent_one = GhostOperative("Spectre", 9)
agent_two = GhostOperative("Phantom", 7)

# 3- EXECUTION: ajanlara emir verelim.
agent_one.report_status()
agent_two.report_status()