# functions : Kod bloklarıdır.
# input alabilir


def hello_python(name): # -> define
    print("hello")
    print(name)
    
hello_python("Ahmet")


# örnekler

def sum_example(num1, num2):
    print(num1 + num2)
    
sum_example(5, 10)

# pratik fonksiyonlar

def divideNumber(number):
    return number / 2

print(divideNumber(20))

myList = [3,5,7,10,20,30]

myResultList = []

for num in myList:
    myResultList.append(divideNumber(num))

print(myResultList)