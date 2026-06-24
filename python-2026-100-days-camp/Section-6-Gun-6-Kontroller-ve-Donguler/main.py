"""
x = 10
y = 5

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

# And, Or, Not

x = True
y = False

print(x and y)
print(x or y)
print(not x)

# Problem
# Bir sistem için kullanıcıların sahip olduğu puanlara göre üyelik
# seviyelerini belirleyen bir kod yazalım.

# kullanıcı puanı
customer_points = 75

# if yapısı
# 100'e eşit veya daha büyükse 
if customer_points >= 100:
    print("Platinum Member")
    
# 50 ile 99 arasındaysa
elif 50 <= customer_points <= 99:
    print("Gold Member")

# 50'den küçük ise
else:
    print("Silver Member")
    

"""

# Döngüler

mylist = [1,2,3,4,5]

for num in mylist:
    print(num)