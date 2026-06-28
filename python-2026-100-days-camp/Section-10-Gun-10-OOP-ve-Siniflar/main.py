class Person():
    # property
    name = ""
    age = 0
    gender = ""

    # initializer method
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        
    # method
    def test(self):
        print("test")