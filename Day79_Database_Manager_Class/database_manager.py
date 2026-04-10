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
        try:
            self.connection = psycopg2.connect(host = self.host, 
                                               dbname = self.name,
                                               user = self.user,
                                               password = self.password,
                                               port = self.port)
            print("Connected to the PostgreSQL server.") 
            
    
        except psycopg2.Error as e:
            print(f" Error type : ({e})")
    
    
    def execute_query(self):
        pass