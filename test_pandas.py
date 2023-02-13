from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd


# choisir les filtres
brand = "BMW"
year_min = 2010
year_max = 2019
power_min = 350
energy = "ess"

url = """https://www.lacentrale.fr/listing?energies={energy}&makesModelsCommercialNames={brand}&powerDINMin={power_min}&yearMax={year_max}&yearMin={year_min}""".format(
brand=brand,energy=energy, power_min=power_min, year_min=year_min, year_max=year_max)

print(url, end='\n''\n')


# Faire une demande GET à l'URL
response = requests.get(url)

# Créer un objet BeautifulSoup à partir de la réponse HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Trouver tous les éléments searchCard
searchCard_elements = soup.find_all(class_='searchCard')   

# Liste pour stocker les données
data_scrap = []

for result in searchCard_elements:
    brand = result.find("h3").text
    model = result.find(class_="Text_Text_text Vehiculecard_Vehiculecard_subTitle Text_Text_body2").text
    year = result.find(class_="Text_Text_text Vehiculecard_Vehiculecard_characteristicsItems Text_Text_body2").text
    year = year.split(" ")[-1] # extraction de l'année seulement
    price = result.find(class_="Text_Text_text Vehiculecard_Vehiculecard_priceContainer Text_Text_body3").text
    location = result.find(class_="Vehiculecard_Vehiculecard_location").text
    a_element = result.find("a")
    link = a_element.get("href")
    

    data_scrap.append([brand, model, year, price, location, link])

# Create a pandas dataframe from the scraped data
df = pd.DataFrame(data_scrap, columns=["Marque", "Modèle", "Année", "Prix", "Département", "Lien"])

# Write the dataframe to a CSV file
df.to_csv("test.csv", index=False)

print("The scraped data has been written to the test.csv file using pandas.")
