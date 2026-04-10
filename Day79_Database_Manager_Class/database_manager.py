import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()



class DatabaseManager:
    
    def __init__(self):
        self.host = os.getenv("DB_HOST")
        self.name = os.getenv("DB_NAME")
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASS")
        self.port = os.getenv("DB_PORT")
        self.connection = None
        
    
    
    def connect(self):
        pass
    
    
    
    
    def execute_query(self):
        pass