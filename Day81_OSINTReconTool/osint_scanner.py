import time
import requests
from bs4 import BeautifulSoup

class OsintScanner:
    
    def __init__(self, target_url):
        self.target_url = target_url

        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
        
        
    def get_html(self):
        try:
            response = requests.get(self.target_url, headers=self.headers)
            return response.text
        except:
            return None
    
    
    def extract_links(self, html_content):
        soup = BeautifulSoup(html_content, "html.parser")
        return [a.get("href") for a in soup.find_all("a") if a.get("href")]