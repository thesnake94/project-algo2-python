"""ce code marche ne marche pas sur mon ubuntu, cause probleme d'installation pandas """
"""marche sur mon windows"""


from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

def format_url(page, brand):
    """on choisi les filtres en déclarant les variables pour l'url"""
    brand = "atchoummmm"
    year_min = 2010
    year_max = 2019
    fuel = ""


    """l'url avec les variables dedans"""
    url = """https://www.lacentrale.fr/listing?energies={fuel}&makesModelsCommercialNames={brand}&options=&page={page}&yearMax={year_max}&yearMin={year_min}""".format(
    brand=brand,fuel=fuel, page=page, year_min=year_min, year_max=year_max,)

    return url

    # """on affiche l'url"""
    # print("Voici l'url de la page scraper :",'\n', url, end='\n''\n')


def main(page, brand) :
    url = format_url(page, brand)


    """faire une demande GET à l'URL"""
    asked = requests.get(url)


    """créer un objet BeautifulSoup à partir de la réponse HTML"""
    soup = BeautifulSoup(asked.text, 'html.parser')


    scrap_card_car = soup.find_all(class_='searchCard')   


    if not scrap_card_car and page == 1 :
        print(f"Aucune voiture de cette marque {brand} n'a été trouvée.", '\n', "Voici l'url de la page : ", url)
        
    else:
        data_list = []


        for scrap in scrap_card_car :

            brand_model = scrap.find("h3") # marque et modele

            motor = scrap.find(class_="Text_Text_text Vehiculecard_Vehiculecard_subTitle Text_Text_body2") # moteur
            price = scrap.find(class_="Text_Text_text Vehiculecard_Vehiculecard_price Text_Text_subtitle2") # prix
            location = scrap.find(class_="Vehiculecard_Vehiculecard_location") # localisation
            year_fuel_mileage = scrap.find_all(class_="Text_Text_text Vehiculecard_Vehiculecard_characteristicsItems Text_Text_body2") # année, energie, kilométrage
            a_element = scrap.find("a")
            link = a_element.get("href") # lien de l'annonce


            if scrap:

                """on créer les variables qui récupèrent seulement les mots que l'on veut dans les variables créées avant"""
                brand_text = brand_model.text.split()[0] # on récupère seulement le premier mot
                model_text = " ".join(brand_model.text.split()[1:]) # on récupère le reste de la chaine de caractere
                year_text = year_fuel_mileage[0].text # extrait le texte du premier élément year de la liste et crée la variable
                mileage_text = year_fuel_mileage[1].text
                fuel_text = year_fuel_mileage[3].text
                

                """on affiche toutes les données récupérées"""
                print(brand_text, model_text, motor.text,'\n', "Année :", year_text,'\n', fuel_text,'\n' , mileage_text,'\n', "Prix :", price.text, '\n',"localisé dans le", location.text, '\n',"url : ", "www.lacentrale.fr" + link, end='\n''\n''\n')
                

                """on converti les chaînes de caractères en entiers (string en int)"""
                price_int = int(price.text.replace(" ", "").replace("€", "")) # supprime les espaces
                year_int = int(year_text) # convertit l'année en int
                mileage_int = int(mileage_text.replace("\xa0", "").replace("km", "")) # supprime les espaces avec "\xa0" 
                location_int = int(location.text)


                """on ajoute les données converties à la liste data_list"""
                df = pd.DataFrame(data_list, columns=["Brand" ,"Model", "Motor", "Year", "Price", "Fuel", "Mileage", "Location"])

    
        if scrap_card_car :
            """Écrire les données dans un fichier CSV"""     
            with open("zebi.csv", "a", newline="") as fd: # ouvre le fichier en mode ajout avec "a"
                df.to_csv(fd, header=not fd.tell(), index=False) # écrire le DataFrame dans le fichier CSV


            print("Voici l'url de la page :", url, '\n', "Toutes ces données ont été écrites dans le fichier cars.csv.", '\n')




if __name__ == "__main__":
    for page in range(1, 4):
        main(page, "")            