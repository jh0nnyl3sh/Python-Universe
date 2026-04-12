import time
import requests
from bs4 import BeautifulSoup

class OsintScanner:
    
    def __init__(self, target_url):
        self.target_url = target_url

        self.headers = {"User-Agent": "Monzilla/5.0 (Windows NT 10.0; Win64; x64)"}
        
        
    def get_html(self):
        pass
    
    
    def extract_links(self, html_content):
        pass