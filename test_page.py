from bs4 import BeautifulSoup
import requests
import csv

# choisir les filtres
brand = "BMW"
year_min = 2010
year_max = 2019
power_min = 350
energy = "ess"

def scrap_listing(brand, year_max, year_min, energy, page_num):
    data_scrap = []
    for i in range(1, page_num + 1):
        url = """https://www.lacentrale.fr/listing?energies={energy}&makesModelsCommercialNames={brand}&powerDINMin={power_min}&yearMax={year_max}&yearMin={year_min}&options=&page={page_num}""".format(
        brand=brand,energy=energy, power_min=power_min, year_min=year_min, year_max=year_max, page_num=i)

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
           a_element = result.find("a")
           link = a_element.get("href")

           if result:
              print(brand.text, model.text,'\n', "Année :", year.text,'\n', "Prix :", price.text, '\n',"localisé dans le", location.text, '\n', "www.lacentrale.fr" + link, end='\n''\n''\n')
              data_scrap.append([brand.text, model.text, year.text, price.text, location.text])
    
    # Écrire les données dans un fichier CSV
    with open("bmw.csv", "w", newline="") as fd:
        writer = csv.writer(fd)
        writer.writerow(["Marque", "Modèle", "Année", "Prix", "Département"]) # Écrire les en-têtes
        for row in data_scrap:
            writer.writerow(row)

    print("Les données scrapé ont été écrites dans le fichier bmw.csv.")
