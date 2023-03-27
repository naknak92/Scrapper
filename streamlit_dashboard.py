# -*- coding: utf-8 -*-

import pymongo
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['products']
collection = db['aliexpress']

data = []
for product in collection.find():
    name = product['name']
    price = product['price']
    data.append({'Nom': name, 'Prix': price})

affichage = st.sidebar.selectbox('Afficher', ['Produits', 'Graphique'])

if affichage == 'Produits':
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

elif affichage == 'Graphique':
    st.sidebar.header('Filtrer les produits pour le graphique')
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
        graphique = st.selectbox('Type de graphique', ['Histogramme', 'Nuage de points', 'Violin plot', 'Box plot'])

        if graphique == 'Histogramme':
            # Créer un histogramme des prix
            prix = [float(d['Prix'].replace('€', '').replace(',', '.')) for d in resultats_filtrage]
            fig, ax = plt.subplots()
            ax.hist(prix, bins=20)
            ax.set_xlabel('Prix (€)')
            ax.set_ylabel('Nombre de produits')
            ax.set_title('Distribution des prix des produits filtrés')
            st.pyplot(fig)

        elif graphique == 'Nuage de points':
            # Créer un nuage de points des prix
            prix = [float(d['Prix'].replace('€', '').replace(',', '.')) for d in resultats_filtrage]
            noms = [d['Nom'] for d in resultats_filtrage]
            fig, ax = plt.subplots()
            ax.scatter(noms, prix)
            ax.set_xlabel('Nom')
            ax.set_ylabel('Prix (€)')
            ax.set_title('Prix des produits filtrés')
            plt.xticks(rotation=90)
            st.pyplot(fig)

        
elif affichage == 'Graphique':
    st.sidebar.header('Filtrer les produits pour le graphique')
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
        graphique = st.selectbox('Type de graphique', ['Histogramme', 'Nuage de points', 'Boxplot'])

        if graphique == 'Histogramme':
            # Créer un histogramme des prix
            prix = [float(d['Prix'].replace('€', '').replace(',', '.')) for d in resultats_filtrage]
            fig, ax = plt.subplots()
            ax.hist(prix, bins=20)
            ax.set_xlabel('Prix (€)')
            ax.set_ylabel('Nombre de produits')
            ax.set_title('Distribution des prix des produits filtrés')
            st.pyplot(fig)

        elif graphique == 'Nuage de points':
            # Créer un nuage de points des prix
            prix = [float(d['Prix'].replace('€', '').replace(',', '.')) for d in resultats_filtrage]
            noms = [d['Nom'] for d in resultats_filtrage]
            fig, ax = plt.subplots()
            ax.scatter(noms, prix)
            ax.set_xlabel('Nom')
            ax.set_ylabel('Prix (€)')
            ax.set_title('Prix des produits filtrés')
            plt.xticks(rotation=90)
            st.pyplot(fig)
            
        elif graphique == 'Boxplot':
            # Créer un boxplot des prix
            prix = [float(d['Prix'].replace('€', '').replace(',', '.')) for d in resultats_filtrage]
            fig, ax = plt.subplots()
            ax.boxplot(prix)
            ax.set_xlabel('Produits filtrés')
            ax.set_ylabel('Prix (€)')
            ax.set_title('Distribution des prix des produits filtrés')
            st.pyplot(fig)
