import requests
from bs4 import BeautifulSoup
from csv import writer
from time import sleep
from random import choice

# list to store scraped data
all_quotes = []

# this part of the url is constant
base_url = "http://quotes.toscrape.com/"

# this part of the url will keep changing
url = "/page/1"

while url:
    
    # concatenating both urls
    # making request
    res = requests.get(f"{base_url}{url}")
    print(f"Now Scraping:{base_url}{url}")
    soup = BeautifulSoup(res.text, "html.parser")
    
    # extracting all elements
    quotes = soup.find_all(class_="quote")
    
    for quote in quotes:
        all_quotes.append({
            "text": quote.find(class_="text").get_text(),
            "author": quote.find(class_="author").get_text(),
            "bio-link": quote.find("a")["href"]
        }) 
        