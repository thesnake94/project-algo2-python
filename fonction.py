from bs4 import BeautifulSoup
import requests
import csv

def main():
    # pour toutes les pages de 1 à 5
    for page in range(1, 6):
        # choisir les filtres en déclarant les variables pour l'url
        brand = "BMW"
        year_min = 2010
        year_max = 2019
        power_min = 350
        fuel = ""

        # l'url avec les variables dedans
        url = """https://www.lacentrale.fr/listing?energies={fuel}&makesModelsCommercialNames={brand}&options=&page={page}&powerDINMin={power_min}&yearMax={year_max}&yearMin={year_min}""".format(
        brand=brand,fuel=fuel, power_min=power_min,page=page, year_min=year_min, year_max=year_max,)

        print("Voici l'url de la page scraper :",'\n', url, end='\n''\n')


        # faire une demande GET à l'URL
        response = requests.get(url)

        # créer un objet BeautifulSoup à partir de la réponse HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # trouver tous les éléments searchCard
        searchCard_elements = soup.find_all(class_='searchCard')   

        # liste pour stocker les données
        data_scrap = []

        # definir les variables tant que les éléments sont dans les card
        for scrap in searchCard_elements:
            brand = scrap.find("h3") # marque
            model = scrap.find("h3") #modele
            motor = scrap.find(class_="Text_Text_text Vehiculecard_Vehiculecard_subTitle Text_Text_body2") # moteur
            price = scrap.find(class_="Text_Text_text Vehiculecard_Vehiculecard_price Text_Text_subtitle2") # prix
            location = scrap.find(class_="Vehiculecard_Vehiculecard_location") # localisation
            year = scrap.find(class_="Text_Text_text Vehiculecard_Vehiculecard_characteristicsItems Text_Text_body2") # année
            fuel = scrap.find_all(class_="Text_Text_text Vehiculecard_Vehiculecard_characteristicsItems Text_Text_body2")[3] # energie
            mileage = scrap.find_all(class_="Text_Text_text Vehiculecard_Vehiculecard_characteristicsItems Text_Text_body2")[1] # kilométrage
            a_element = scrap.find("a")
            link = a_element.get("href") # lien de l'annonce

            if scrap:

                # on créer les variables qui récupèrent seulement les mots que l'on veut dans les variables créées avant
                brand_text = brand.text.split()[0] # pour la variable brand on récupère seulement le premier mot pour la marque
                model_text = " ".join(model.text.split()[1:]) # pour la variable model on récupère le reste des mots apres le premier du h3 pour le modele

                # on affiche toutes les données récupérées
                print(model.text, motor.text,'\n', "Année :", year.text,'\n', fuel.text,'\n' , mileage.text,'\n', "Prix :", price.text, '\n',"localisé dans le", location.text, '\n', "www.lacentrale.fr" + link, end='\n''\n''\n')
                

                # on converti les chaînes de caractères en entiers (string en int)
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
    main()
    scrap_print()
