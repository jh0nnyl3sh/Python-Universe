# employees.py dosyasından 'employees' List verisini import ediyoruz.
from employees import employees

def calculate_department_salary(data, target_department):
    """
    Belirli bir departmandaki çalışanların toplam maaşını hesaplayan function.
    
    Parameters:
    data (List): İçinde çalışanların bilgilerini (Dictionary) tutan liste.
    target_department (String): Maaş toplamı hesaplanacak hedef departman.
    
    Returns:
    int: Hedef departmandaki toplam maaş miktarı.
    """
    
    # Toplam maaşı tutacağımız variable'ı sıfırdan başlatıyoruz.
    # Scope kuralları gereği function içinde tanımlanması zorunludur.
    total_salary = 0
    
    # Gelen 'data' List'i içindeki her bir 'employee' Dictionary'si için loop başlatıyoruz.
    for employee in data:
        # O anki çalışanın 'department' value'su, hedef departmanımızla eşleşiyor mu kontrol ediyoruz.
        if target_department == employee["department"]:
            # Eğer eşleşiyorsa, çalışanın 'salary' value'sunu total_salary variable'ına ekliyoruz.
            total_salary += employee["salary"]
            
    # Loop bittikten sonra, hesaplanan toplam maaşı function'dan dışarı fırlatıyoruz (return).
    return total_salary


# Hedef departmanımızı belirliyoruz.
target_department = "IT"

# Function'ı çağırıp, return edilen değeri 'sonuc' adlı variable'da yakalıyoruz.
sonuc = calculate_department_salary(employees, target_department)

# Çıkan sonucu formatlı bir şekilde ekrana yazdırıyoruz.
print(f"[{target_department}] departmanının toplam maaş gideri: {sonuc}")