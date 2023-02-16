from bs4 import BeautifulSoup
import requests
import csv

def format_url(page, brand):
    """on choisi les filtres en déclarant les variables pour l'url"""
    brand = "BMW"
    year_min = 2010
    year_max = 2019
    fuel = ""
    power_min = "500"

    """l'url avec les variables dedans"""
    url = "https://www.lacentrale.fr/listing?energies={fuel}&makesModelsCommercialNames={brand}&options=&page={page}&powerDINMin={power_min}&yearMax={year_max}&yearMin={year_min}".format(
    brand = brand, fuel = fuel, page = page, year_min = year_min, year_max = year_max, power_min = power_min)

    return url


"""fonction main qui rappelle les variables page et brand"""
def main(page, brand) :
    url = format_url(page, brand)


    """faire une demande GET à l'URL"""
    asked = requests.get(url)


    """créer un objet BeautifulSoup à partir de la réponse HTML"""
    soup = BeautifulSoup(asked.text, 'html.parser')


    """extrait les éléments de cette classe"""
    scrap_card_car = soup.find_all(class_='searchCard')   


    """vérifie s'il trouve des searchCard"""
    if not scrap_card_car and page == 1 :
        print("Aucune voiture n'a été trouvée.", '\n', f"Voici l'url de la page : {url}")
        

    else:
        data_list = []


        for scrapper in scrap_card_car :

            brand_model = scrapper.find("h3") # marque et modele
            motor = scrapper.find(class_="Text_Text_text Vehiculecard_Vehiculecard_subTitle Text_Text_body2") # moteur
            price = scrapper.find(class_="Text_Text_text Vehiculecard_Vehiculecard_price Text_Text_subtitle2") # prix
            location = scrapper.find(class_="Vehiculecard_Vehiculecard_location") # localisation
            year_fuel_mileage = scrapper.find_all(class_="Text_Text_text Vehiculecard_Vehiculecard_characteristicsItems Text_Text_body2") # année, energie, kilométrage
            a_element = scrapper.find("a")
            link = a_element.get("href") # lien de l'annonce


            if scrapper:

                """on créer les variables qui récupèrent seulement les mots que l'on veut dans les variables créées avant"""
                brand_text = brand_model.text.split()[0]
                model_text = " ".join(brand_model.text.split()[1:])
                year_text = year_fuel_mileage[0].text
                mileage_text = year_fuel_mileage[1].text
                fuel_text = year_fuel_mileage[3].text
                

                """on affiche toutes les données récupérées"""
                print(brand_text, model_text, motor.text,'\n', "Année :", year_text,'\n', fuel_text,'\n' , mileage_text,'\n', "Prix :", price.text, '\n',"localisé dans le", location.text, '\n',"url : ", "https://www.lacentrale.fr" + link, end='\n''\n''\n')
                

                """on converti les chaînes de caractères en entiers (string en int)"""
                price_int = int(price.text.replace(" ", "").replace("€", ""))
                year_int = int(year_text)
                mileage_int = int(mileage_text.replace("\xa0", "").replace("km", ""))
                location_int = int(location.text)


                """on ajoute les données converties à la liste data_list"""
                data_list.append([brand_text, model_text, motor.text, year_int, price_int, fuel_text, mileage_int, location_int])

    
        if scrap_card_car :
            """Écrire les données dans un fichier CSV"""
            with open("cars.csv", "a", newline='') as fd :
                writer = csv.writer(fd)
                writer.writerow(["Brand" ,"Model", "Motor", "Year", "Price", "Fuel", "Mileage", "Location"])
                for row in data_list: 
                    writer.writerow(row)

            print(f"Voici l'url de la page n° {page} : {url}" '\n', "Toutes ces données ont été écrites dans le fichier cars.csv.", '\n')


if __name__ == "__main__":
    for page in range(1, 4):
        main(page, "")