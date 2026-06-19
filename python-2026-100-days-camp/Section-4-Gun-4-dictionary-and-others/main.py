# Dictionary
# A dictionary is a collection of unordered, modifiable (mutable)
# paired (key:value) data type.

# Creating a dictionary
# To create a dictionary we use curly brackets, {}
# or the dict() buit-in function.

# syntax
empty_dict = {}
# Dictionary with data values
dct = {"key1": "value1", "key2": "value2", "key3": "value3"}


# Example
person = {
    "first_name": "John",
    "last_name": "Lesh",
    "age": 30,
    "country": "USA",
    "is_married": True,
    "skills": ["Python", "JavaScript", "C++"],
    "address": {
        "street": "123 Main St",
        "city": "New York",
        "state": "NY",
        "zip_code": "10001"
    }
}

# Accessing dictionary items
# We can access Dictionary items by referring to its key name.
# syntax
dct = {"key1": "value1", "key2": "value2", "key3": "value3"}
print(dct["key1"]) # value1
print(dct["key2"]) # value2

# Example
person = {
    "first_name": "John",
    "last_name": "Lesh",
    "age": 30,
    "country": "USA",
    "is_married": True,
    "skills": ["Python", "JavaScript", "C++"],
    "address": {
        "street": "123 Main St",
        "city": "New York",
        "state": "NY",
        "zip_code": "10001"
    }
}

print(person["first_name"]) # John
print(person["last_name"]) # Lesh
print(person["age"]) # 30
print(person["country"]) # USA
print(person["is_married"]) # True
print(person["skills"]) # ['Python', 'JavaScript', 'C++']
print(person["address"]) # {'street': '123 Main St', 'city': 'New York', 'state': 'NY', 'zip_code': '10001'} 
