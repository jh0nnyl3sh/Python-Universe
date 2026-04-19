"""
📜 SEVİYE 1 GÖREVİ: "Dava Masraf ve Kategori Motoru"
Senaryo: Adliyede açılan yeni bir davanın başlangıç masrafını ve
bu davanın Adli Tıp Kurumu'na (ATK) gidip gitmeyeceğini sisteme
gireceğiz. Sistem bize toplam masrafı hesaplayıp, davanın hangi
bütçe kategorisinde olduğunu Print ile ekrana basacak.

* Senden İstenenler (Requirements):
-İki adet Variable tanımla: base_cost (Davanın taban masrafı - Integer
veya Float bir değer ver. Örn: 1500)

-needs_expert (Bilirkişi/ATK gerekiyor mu? - Boolean olarak True
veya False ver).

-Bir If bloğu ile kontrol et: EĞER needs_expert durumu True ise,
base_cost üzerine 3000 (bilirkişi ücreti) ekle.

-Sonra yeni bir If-Elif-Else yapısı kurarak toplam masrafı kontrol
et:

    Toplam masraf 5000'den büyükse: 
    Ekrana "Kategori A: Yüksek Masraflı Dava" yazdır.
    
    Toplam masraf 3000 ile 5000 arasındaysa (5000 dahil): 
    Ekrana "Kategori B: Orta Masraflı Dava" yazdır.
    
    Toplam masraf 3000'den küçükse: 
    Ekrana "Kategori C: Düşük Masraflı Dava" yazdır.

"""
print("-" * 50)
print("Dava Masraf ve Kategori Motoru")
print("-" * 50)


base_cost = 1000 # Dosya ücreti
needs_expert = True # Bilirkişi/ATK gerekli mi ?

# Bilirkişi/ATK gerekiyor ise:
if needs_expert:
    base_cost += 3000 # (bilirkişi ücreti)
    
# Dosya kategorisi belirleme
if base_cost > 5000:
    print("Kategori A: Yüksek Masraflı Dava")
elif base_cost >= 3000:
    print("Kategori B: Orta Masraflı Dava")
else:  
    print("Kategori C: Düşük Masraflı Dava")