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


# Vérifier que la demande a été réussie
if response.status_code == 200:
   # Créer un objet BeautifulSoup à partir de la réponse HTML
   soup = BeautifulSoup(response.text, 'html.parser')


   # Trouver tous les éléments searchCard
   searchCard_elements = soup.find_all(class_='searchCard')

   for result in searchCard_elements:
       brand = result.find("h3")
       if brand:
          print(brand.text)

       model = result.find(class_="Text_Text_text Vehiculecard_Vehiculecard_subTitle Text_Text_body2")
       if model:
          print(model.text)

       year = result.find(class_="Vehiculecard_Vehiculecard_characteristics")
       if year:
          print(year.text, end='\n')

       price = result.find(class_="Text_Text_text Vehiculecard_Vehiculecard_priceContainer Text_Text_body3")
       if price:
          print(price.text, end='\n''\n''\n')
   
else:
   print("Il y a une erreur quelque part. Le code est erreur est : ",
         response.status_code)
