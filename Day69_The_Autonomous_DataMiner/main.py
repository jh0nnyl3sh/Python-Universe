import requests
import csv 


class DataMiner:
    
    # Attribute
    def __init__(self, target_url):
        self.target_url = target_url
        self.intel_data = [] # -> çekilen veriler burada duracak
    
