import os
import psycopg2
from dotenv import load_dotenv

# Ortam değişkenlerini sisteme yükle
load_dotenv()

class DatabaseManager:
    
    def __init__(self):
        # Bağlantı bilgilerini dış dünyadan izole şekilde hafızaya al
        self.host = os.getenv("DB_HOST")
        self.dbname = os.getenv("DB_NAME") 
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASS")
        self.port = os.getenv("DB_PORT")
        
        # Başlangıçta bağlantı kapalı
        self.connection = None
        
    def connect(self):
        """Veritabanına bağlanır ve bağlantıyı aktif tutar."""
        try:
            self.connection = psycopg2.connect(
                host=self.host, 
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                port=self.port
            )
            print("🟢 Veritabanına başarıyla bağlanıldı!") 
            
        except psycopg2.Error as e:
            print(f"🔴 Veritabanı bağlantı hatası: {e}")
    
    def execute_query(self, query, params=None):
        """Sorguları güvenli bir şekilde (SQL Injection Korumalı) çalıştırır."""
        
        # Bağlantı açılmamışsa uyarı ver
        if not self.connection:
            print("🔴 Lütfen önce connect() metodunu çalıştırın!")
            return None

        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            
            # KARAR MEKANİZMASI (Vitesler)
            if query.strip().upper().startswith("SELECT"):
                # Veri okuma işlemiyse: Verileri al ve döndür
                result = cursor.fetchall()
                return result
            else:
                # Veri yazma (INSERT/UPDATE/DELETE) işlemiyse: Kaydet
                self.connection.commit()
                print("🟢 İşlem başarıyla kaydedildi!")
                return True
                
        except Exception as e:
            # Hata durumunda veritabanının kilitlenmemesi için işlemi geri al
            print(f"🔴 Sorgu hatası: {e}")
            self.connection.rollback()
            return False
            
        finally:
            # İşlem bitince imleci mutlaka kapat
            cursor.close()

    def close_connection(self):
        """Tüm işlemler bittiğinde veritabanı bağlantısını güvenlice kapatır."""
        if self.connection:
            self.connection.close()
            print("⚪ Veritabanı bağlantısı sonlandırıldı.")
            
            


# Sınıfı çağır ve hafızayı oluştur
db = DatabaseManager()

# Bağlantıyı aç
db.connect()


# Kapıyı kilitleyip çık
db.close_connection()