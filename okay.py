from bs4 import BeautifulSoup
import requests


# choisir les filtres
brand = "BMW"
year_min = 2010
year_max = 2019
power_min = 350
energies = "ess"
url = """https://www.lacentrale.fr/listing?energies={energies}&makesModelsCommercialNames={brand}&powerDINMin={power_min}&yearMax={year_max}&yearMin={year_min}""".format(
brand=brand,energies=energies, power_min=power_min, year_min=year_min, year_max=year_max)

print(url, end='\n''\n')



# Faire une demande GET à l'URL
response = requests.get(url)


# Créer un objet BeautifulSoup à partir de la réponse HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Trouver tous les éléments searchCard
searchCard_elements = soup.find_all(class_='searchCard')   

for result in searchCard_elements:
   brand = result.find("h3")
   model = result.find(class_="Text_Text_text Vehiculecard_Vehiculecard_subTitle Text_Text_body2")
   year = result.find(class_="Text_Text_text Vehiculecard_Vehiculecard_characteristicsItems Text_Text_body2")
   price = result.find(class_="Text_Text_text Vehiculecard_Vehiculecard_priceContainer Text_Text_body3")
   location = result.find(class_="Vehiculecard_Vehiculecard_location")
   if result:
      print(brand.text, model.text, year.text,'\n', "Prix :", price.text, '\n',"localisé dans le", location.text, end='\n''\n')


