import tkinter as tk
from bs4 import BeautifulSoup
import requests


def scrape_data():
    brand = "BMW"
    year_min = 2010
    year_max = 2019
    url = """https://www.lacentrale.fr/listing?makesModelsCommercialNames={brand}&yearMax={year_max}&yearMin={year_min}""".format(
        brand=brand, year_min=year_min, year_max=year_max)

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        search_card_elements = soup.find_all(class_='searchCard')
        data = []
        for search_card in search_card_elements:
            data.append(search_card.text.split("\n"))
        display_data(data)
    else:
        print("Il y a une erreur quelque part. Le code est erreur est : ", response.status_code)


def display_data(data):
    root = tk.Tk()
    root.title("Data Scraped")
    for i, row in enumerate(data):
        for j, column in enumerate(row):
            label = tk.Label(root, text=column, borderwidth=1, relief="solid")
            label.grid(row=i, column=j)
    root.mainloop()


if __name__ == '__main__':
    scrape_data()
