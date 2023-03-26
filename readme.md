# Scraper des produits Aliexpress et les afficher avec Streamlit
Ce projet consiste en un scraper de produits Aliexpress qui récupère le nom et le prix des produits à partir de la page Web d'Aliexpress et les stocke dans une base de données MongoDB. Les données sont ensuite récupérées à partir de la base de données et affichées dans un tableau avec Streamlit.

# Le code se compose de trois parties 

- aliexpress_scrapper.py : ce fichier contient le code qui effectue le scraping des données à partir de la page Web d'Aliexpress et les stocke dans une base de données MongoDB.
- streamlit_dashboard.py : ce fichier contient le code qui récupère les données de la base de données et les affiche dans un tableau avec Streamlit.
- test_unitaire.py : ce fichier contient des tests unitaires pour les fonctions de scraping et d'affichage des données.

# Comment utiliser ce code 

Assurez-vous d'avoir Python 3.x et les bibliothèques suivantes installées : pymongo, requests, BeautifulSoup et streamlit.
Lancez le fichier aliexpress_scrapper.py pour scraper les données et les stocker dans la base de données MongoDB.
Lancez le fichier streamlit_dashboard.py avec la commande "streamlit run (nom du fichier) pour afficher les données dans un tableau avec Streamlit.
Lancez le fichier test_unitaire.py pour exécuter les tests unitaires.