import pdfplumber
import pandas as pd

# PDF Parsing (Data Extraction) Method'u
def pdf_to_dataframe(pdf_yolu):
    print(f"\n[🚀] {pdf_yolu} dosyası için PDF Parsing başlatılıyor...")

    # Context Manager (with) kullanarak dosyayı açıyoruz.
    # Bu yöntem, işlem bitince dosyayı otomatik kapatır ve memory leak (hafıza sızıntısı) oluşmasını engeller
    with pdfplumber.open(pdf_yolu) as pdf:
        
        # Sadece ilk sayfayı (0. Index) alalım
        ilk_sayfa = pdf.pages[0]
        
        # Sayfadaki tabloyu Extract et (Arka planda bize bir list of lists döndürür)
        tablo = ilk_sayfa.extract_table()
        
        if tablo:
            # tablonun 0. Index'i Header (Sütun Başlıkları) olur.
            # 1. Index'ten sonrası ise Data kısmıdır.
            df = pd.DataFrame(tablo[1:], columns=tablo[0])
            
            # --- TEMİZLİK FİLTRESİ ----
            # 1. hücrelerdeki sadece boşluktan ibaret olan veya tamamen boş olan stringleri nan objesine çevirir
            df = df.replace(r'^\s*$', pd.NA, regex=True)
            
            # 2. içi tamamen boş (nan) olan o hayalet satırları buharlaştır
            df = df.dropna(how='all')
            
            # 3. Index numaralarını yeniden düzenle
            df = df.reset_index(drop=True)
            
            print("[+] PDF başarıyla parlaçandı ve DataFrame Object'ine çevrildi!")
            print("-" * 50)
            return df
        else:
            print("[-] Bu PDF sayfasında tablo bulunamadı (Unstructured Data).")
            return None
        
# ------ MAIN ------
if __name__ == "__main__":
    
    # 1. Hedef dosyanın yolu
    hedef_dosya = 'sahte_rapor.pdf'

    # 2. Method'u ateşle ve dönen değeri bir değişkende yakala
    sonuc_df = pdf_to_dataframe(hedef_dosya)
    
    # 3. Eğer None dönmediyse, ekrana bas
    if sonuc_df is not None:
        print(sonuc_df)
        print("-" * 50)
        
        
