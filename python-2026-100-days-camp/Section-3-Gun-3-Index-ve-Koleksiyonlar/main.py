# Index Mantığı
name = "Johnny Lesh"
print(name[0])
print(len(name)-1)
print(name[-1])



# Slicing
# Slicing, bir dizinin veya listenin belirli bir bölümünü almak 
# için kullanılan bir tekniktir. Python'da slicing,
# köşeli parantezler [] içinde iki nokta üst üste (:) kullanılarak 
# yapılır.

# name[start:end:step]

print(name[:3:])
print(name[3:6:])
print(name[6:9:2])

# Slicing Örnekleri
# Slicing örnekleri olarak, bir dizinin veya
# listenin belirli bir bölümünü almak için kullanılan
# slicing tekniğini göstermek için birkaç örnek verilebilir.
# Örneğin, bir dizi veya listeyi belirli bir aralıkta kesmek için
# slicing kullanılabilir.
barkod = "ABCD1234EFGH5678IJKL"
print(barkod[4:8])  # 1234



# Liste Nedir ?
"""
- Listeler (Python'da lists), birden fazla veriyi bir arada saklayabilen,
sıralı ve değiştirilebilir veri yapılarıdır.
- Listeler, aynı türden veya farklı türlerden öğeler barındırabilirler.
- Listeler değiştirilebilir (mutable)dir.

"""


myList = [1, 2, 3, 4, 5]
print(myList)
print(type(myList))


myList.sort() # -> sıralama işlemi yapar
myList.append(6) # -> listeye yeni bir eleman ekler
myList.insert(0, 0) # -> belirli bir konuma yeni bir eleman
myList.remove(3) # -> listeden belirli bir elemanı kaldırır
myList.pop() # -> listeden son elemanı kaldırır
myList.clear() # -> listeden tüm elemanları kaldırır



# Veri Tipi Dönüştürme

x = 10
print(type(x)) # -> <class 'str'>

y = str(x)
print(type(y)) # -> <class 'str'>

# Daha İleri Seviye Listeler 
# Bu bölümde, programalma dilinde listelerin daha ileri seviye
# kullanımı ele alınıyor.

# Liste oluşturma : Farklı türlerde (string, integer, float, mix) listeler
# oluşturulabilir.
my_list = [1, 2, 3, 4, 5, "a", "b", "c", 3.14, 2.718]

# Liste İşlemleri
# Listeler üzerinde toplama ve çarpma işlemleri yapılabilir.
list1 = [1, 2, 3]
list2 = [4, 5, 6]
# Toplama işlemi
result = list1 + list2
print(result)  # Output: [1, 2, 3, 4, 5, 6]
# Çarpma işlemi
result = list1 * 2
print(result)  # Output: [1, 2, 3, 1, 2, 3]

# İç İçe Listeler
# Erişim Yöntemleri
# Dilimleme (Slicing)