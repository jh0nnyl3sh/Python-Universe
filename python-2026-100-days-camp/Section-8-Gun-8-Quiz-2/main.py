# 1) Aşağıdaki kodun çıktısı ne olacaktır?
x = 5
y = 3
z = 6
x > y and z > x

# cevap
print(f"1. Sorunun Cevabı : {x > y and z > x}") # True




# 2) Aynı değerlerle kod şu şekilde değiştilirse çıktı ne olacaktır?
x < y or z > y

# cevap
print(f"2. Sorunun cevabı : {x < y or z > y}") # True




# 3) Aşağıdaki kodun çıktısı ne olacaktır?
'''
yas = 20

if yas < 18:
    print("18 yaşından küçüksünüz")
elif yas >= 18 and yas < 30:
    print("18 ile 30 yaş arasında bir gençsiniz")
elif yas >= 30 and yas < 40:
    print("30 ve 40 arasına gelmişsiniz")
else:
    print("40 yaşından daha büyüksünüz")
'''
"""
\nyas = 20\n
\nif yas < 18:
\n print("18 yaşından küçüksünüz")
\nelif yas >= 18 and yas < 30:\n
print("18 ile 30 yaş arasında bir gençsiniz")
\nelif yas >= 30 and yas < 40:\n
print("30 ve 40 arasına gelmişsiniz")\n
else:\nprint("40 yaşından daha büyüksünüz")\n"""

# cevap
yas = 20

if yas < 18:
    print("3. Sorunun cevabı : 18 yaşından küçüksünüz")
elif yas >= 18 and yas < 30:
    print("3. Sorunun cevabı : 18 ile 30 yaş arasında bir gençsiniz")
elif yas >= 30 and yas < 40:
    print("3. Sorunun cevabı : 30 ve 40 arasına gelmişsiniz")
else:
    print("3. Sorunun cevabı : 40 yaşından daha büyüksünüz")
    





#4) Aşağıdaki sözlükte, değerler içinde c harfinin geçip geçmediğini gösteren bir if koşulu yazınız
my_dictionary = {"k1":10,"k2k":"a","k32":30,"k4":"c"}
# cevap
# cevap
print("4. Sorunun cevabı : ")
for letter in my_dictionary.values():
    if letter == "c".lower():
        print(f"- Uygun harf bulundu {letter}")
    





#5) Aşağıdaki sözlükte, anahtarlar içinde a harfinin geçip geçmediğini gösteren bir if koşulu yazınız
my_other_dictionary = {"b":203,"c":"a","a":400,"d":"f"}
# cevap
# cevap
print("5. Sorunun cevabı: ")
for l in my_other_dictionary.keys():
    if l == "a".lower():
        print(f"- Uygun harf bulundu : {l}")



#6) Aşağıdaki listedeki sayılardan sadece çift sayı olanları yazdıran bir kod yazınız.
my_numbers = [1,2,3,4,5,6,19,20,32,21,20,1111,23,24]
# cevap
# cevap
# cevap

print("6. Sorunun cevabı: ")
for num in my_numbers:
    if num % 2 == 0:
        print(f"- {num} sayısı çifttir.")




#7) Aşağıdaki listedeki sayılar bir dairenin yarı çapını vermektedir. 
#Tüm dairelerin çevresini içeren başka yeni bir liste oluşturunuz. (İpucu: 2 * pi * r)  Pi 3.14 alınabilir.
r_list = [3,2,5,8,4,6,9,12]
# cevap
# cevap
# cevap
#8) Aşağıdaki listede isim - yaş eşleşmelerinin bulunduğu yapılar mevcuttur.
# Sadece yaşların olduğu yeni ve ayrı bir liste oluşturunuz.
age_name_list = [("Ahmet",30),("Ayse",24),("Mehmet",40),("Fatma",29)]
# cevap
# cevap
# cevap
#9) Aşağıdaki müzik gruplarından birini rastgele yazdıran bir kod yazınız
metal_list = ["Metallica","Iron Maiden","Dream Theater","Megadeth","AC/DC"]
# cevap
# cevap
# cevap
#10) Aşağıdaki kodun çıktısı ne olacaktır?
number_list = [5,7,18,21,20,10,405,24]
[num % 2 == 0 for num in number_list]

# cevap
# cevap
# cevap
