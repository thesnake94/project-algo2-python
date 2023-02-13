from bs4 import BeautifulSoup
import requests


# choisir marque et année min et max de la voiture
brand = "BMW"
year_min = 2010
year_max = 2019
power_min = 250
url = """https://www.lacentrale.fr/listing?makesModelsCommercialNames={brand}&powerDINMin={power_min}&yearMax={year_max}&yearMin={year_min}""".format(
brand=brand,power_min=power_min, year_min=year_min, year_max=year_max)

print(url)


# partie scrap


# Faire une demande GET à l'URL
response = requests.get(url)


# Vérifier que la demande a été réussie
if response.status_code == 200:
   # Créer un objet BeautifulSoup à partir de la réponse HTML
   soup = BeautifulSoup(response.text, 'html.parser')


   # Trouver tous les éléments searchCard
   search_card_elements = soup.find_all(class_='searchCard')


   # Imprimer le texte de chaque searchCard
   for search_card in search_card_elements:
       print(search_card.text, end='\n''\n')
else:
   print("Il y a une erreur quelque part. Le code est erreur est : ",
         response.status_code)
