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



st.sidebar.header('Filtrer les produits')
filtre_nom = st.sidebar.text_input('Nom')
filtre_prix_min = st.sidebar.number_input('Prix minimum', value=0)
filtre_prix_max = st.sidebar.number_input('Prix maximum', value=9999999)



resultats_filtrage = []
for product in collection.find():
    name = product['name']
    price = product['price']
    if filtre_nom.lower() in name.lower() and filtre_prix_min <= float(price.replace('€', '').replace(',', '.')) <= filtre_prix_max:
        resultats_filtrage.append({'Nom': name, 'Prix': price})


if resultats_filtrage:
    st.write('Résultats du filtrage')
    st.table(resultats_filtrage)
else:
    st.write('Aucun produit ne correspond aux critères de filtrage.')
