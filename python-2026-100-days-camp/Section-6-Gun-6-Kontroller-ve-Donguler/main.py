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
"""
mylist = [1,2,3,4,5]

for num in mylist:
    print(num)
    
"""    

"""
mylist = [10, 20, 30, 40, 50, 60, 70]

print
print("Lsitemizde 6'ya tam bölünen sayılar : ")
for num in mylist:
    if num % 6 == 0:
        print(num)
        
"""


"""
my_string = "hello world"

for l in my_string:
    print(l)

    


my_tuple = (10, 20, 30, 40, 50, 60)

for num in my_tuple:
    print(num / 5 * 2)
"""    

    
my_new_list = [("a","b"),("c","d"),("e","f"),("g","h")]

print(len(my_new_list))

for element in my_new_list:
    print(element)
    
    
for(x,y) in my_new_list:
    print(x)
    print(y)