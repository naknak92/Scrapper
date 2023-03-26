import pymongo
import streamlit as st


client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['products']
collection = db['aliexpress']


data = []
for product in collection.find():
    name = product['name']
    price = product['price']
    data.append({'Nom': name, 'Prix': price})


st.write('Liste des produits')
st.table(data)
