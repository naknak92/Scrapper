import pymongo
import requests
from bs4 import BeautifulSoup


client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['products']
collection = db['aliexpress']

url = 'https://fr.aliexpress.com/category/205006047/Cellphones.html?category_redirect=1&spm=a2g0o.home.103.2.2eeb7065h4g2LF'
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')


products = soup.find_all('div', class_='manhattan--content--1KpBbUi')


for product in products:
    name = product.find('h1', class_='manhattan--titleText--WccSjUS').text.strip()
    price = product.find('div', class_='manhattan--price-sale--1CCSZfK').text.strip()
    data = {'name': name, 'price': price}
    collection.insert_one(data)
