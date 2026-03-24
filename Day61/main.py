import requests

target_url = "https://jsonplaceholder.typicode.com/users/1"

def fetch_user_intel(url):
    
    response = requests.get(url)
    
    if response.status_code == 200:
        
        data = response.json()
        user_name = data["name"]
        user_email = data["email"]
        user_address = data["address"]["city"]
        

        print("🎯 TARGET SECURED!")
        print(f"Name: {user_name}")
        print(f"Email: {user_email}")
        print(f"City: {user_address}")
    
    else:
        print("🚨 Hedef sunucuya ulaşılamadı")
        

        
fetch_user_intel(target_url)