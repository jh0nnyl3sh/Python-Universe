# 1. Problem 

# string bir değişken
user_age = "28"

# string'i integer'a çevirip yeni bir değişkene atadık
user_age_int = int(user_age)
print(type(user_age_int))

# değişkene ekleme yaptık.
new_user_age = user_age_int + 5
print(new_user_age)

# yeniden string'e çevirip ekrana yazdırdık.
new_user_age_str = str(new_user_age)
print(type(new_user_age_str))

# 2. Problem
# index ile listeden veri çıkarmak
my_list = [10, 20, 30, 40, 50, 60, 70]
print(f"4. Eleman : {my_list[3]}")

# slicing ile listeden belirli bir aralıkta veri çıkarmak
my_list2 = my_list[:5]
print(f"İlk 5 Eleman : {my_list2}")


# 3. Problem
my_dct = {"username": "developer", "is_active": True}

# is_active anahtarının değerini False olarak güncelle
my_dct["is_active"] = False
print(my_dct)

# Problem 4
data = [1, 2, 2, 3, 4, 4, 5]
new_data = set(data)
print(new_data)

new_data = tuple(new_data)
print(new_data)
print(type(new_data))
