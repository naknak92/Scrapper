import unittest
import pymongo
import requests
from bs4 import BeautifulSoup
import streamlit as st

class TestProductScraper(unittest.TestCase):
    
    def setUp(self):
        
        self.client = pymongo.MongoClient('mongodb://localhost:27017/')
        self.db = self.client['products']
        self.collection = self.db['test']
        
      
        self.collection.insert_many([
            {'name': 'Test Product 1', 'price': '$10'},
            {'name': 'Test Product 2', 'price': '$20'},
            {'name': 'Test Product 3', 'price': '$30'},
        ])
        
    def test_product_scraper(self):
       
        url = 'https://fr.aliexpress.com/category/205006047/Cellphones.html?category_redirect=1&spm=a2g0o.home.103.2.2eeb7065h4g2LF'
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.143 Safari/537.36'}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        products = soup.find_all('div', class_='manhattan--content--1KpBbUi')
        for product in products:
            name = product.find('h1', class_='manhattan--titleText--WccSjUS').text.strip()
            price = product.find('div', class_='manhattan--price-sale--1CCSZfK').text.strip()
            data = {'name': name, 'price': price}
            self.collection.insert_one(data)
       
    
    def test_product_display(self):
        
        with st.echo(code_location='below'):
            data = []
            for product in self.collection.find():
                name = product['name']
                price = product['price']
                data.append({'Nom': name, 'Prix': price})
            st.write('Liste des produits')
            st.table(data)
        self.assertEqual(len(data), 3)
        
    def tearDown(self):
        
        self.collection.delete_many({})
        self.client.close()
        
if __name__ == '__main__':
    unittest.main()
