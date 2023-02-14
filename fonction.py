from bs4 import BeautifulSoup
import requests
import csv
# import pandas as pd


def scrap_url():
    for page in range(1, 5):
    # choisir les filtres
        brand = "BMW"
        year_min = 2010
        year_max = 2019
        power_min = 350
        fuel = ""
        url = """https://www.lacentrale.fr/listing?energies={fuel}&makesModelsCommercialNames={brand}&options=&page={page}&powerDINMin={power_min}&yearMax={year_max}&yearMin={year_min}""".format(
        brand=brand,fuel=fuel, power_min=power_min,page=page, year_min=year_min, year_max=year_max,)

        print("Voici l'url de la page scraper :",'\n', url, end='\n''\n')


        # Faire une demande GET à l'URL
        response = requests.get(url)

        # Créer un objet BeautifulSoup à partir de la réponse HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Trouver tous les éléments searchCard
        searchCard_elements = soup.find_all(class_='searchCard')   

   # Liste pour stocker les données
        data_scrap = []


        for result in searchCard_elements:
            brand = result.find("h3")
            model = result.find("h3")
            motor = result.find(class_="Text_Text_text Vehiculecard_Vehiculecard_subTitle Text_Text_body2")
            price = result.find(class_="Text_Text_text Vehiculecard_Vehiculecard_price Text_Text_subtitle2")
            location = result.find(class_="Vehiculecard_Vehiculecard_location")
            year = result.find(class_="Text_Text_text Vehiculecard_Vehiculecard_characteristicsItems Text_Text_body2")
            fuel = result.find_all(class_="Text_Text_text Vehiculecard_Vehiculecard_characteristicsItems Text_Text_body2")[3]
            mileage = result.find_all(class_="Text_Text_text Vehiculecard_Vehiculecard_characteristicsItems Text_Text_body2")[1]
            a_element = result.find("a")
            link = a_element.get("href")

            if result:
                brand_text = brand.text.split()[0]
                model_text = " ".join(model.text.split()[1:])

                print(model.text, motor.text,'\n', "Année :", year.text,'\n', fuel.text,'\n' , mileage.text,'\n', "Prix :", price.text, '\n',"localisé dans le", location.text, '\n', "www.lacentrale.fr" + link, end='\n''\n''\n')
                

                # Convertir les chaînes de caractères en entiers
                price_int = int(price.text.replace(" ", "").replace("€", ""))
                year_int = int(year.text)
                mileage_str = mileage.text.strip().replace("\xa0", "").replace("km", "")
                mileage_int = int(mileage_str)
                location_int = int(location.text)

                # Ajouter les données converties à la liste data_scrap
                data_scrap.append([brand_text, model_text, motor.text, year_int, price_int, fuel.text, mileage_int, location_int])

        

    # Écrire les données dans un fichier CSV
        with open("zebi.csv", "a", newline="") as fd:
            writer = csv.writer(fd)
            writer.writerow(["Marque" ,"Modèle", "Motorisation", "Année", "Prix en €", "Energie", "Kilométrage", "Département"]) # Écrire les en-têtes
            for row in data_scrap:
                writer.writerow(row)

def scrap_print():
    print("Les données scrapé ont été écrites dans le fichier zebi.csv.")

if __name__ == "__main__":
    scrap_url()
    scrap_print()
