import wx
import requests
from bs4 import BeautifulSoup

brand = "BMW"
year_min = 2010
year_max = 2019
url = "https://www.lacentrale.fr/listing?makesModelsCommercialNames={brand}&yearMax={year_max}&yearMin={year_min}".format(
    brand=brand, year_min=year_min, year_max=year_max)

# faire une demande GET à l'URL
response = requests.get(url)

# vérifier que la demande a été réussie
if response.status_code == 200:
    # créer un objet BeautifulSoup à partir de la réponse HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # trouver tous les éléments searchCard
    search_card_elements = soup.find_all(class_='searchCard')

    # récupérer le texte de chaque searchCard
    data = [search_card.text for search_card in search_card_elements]
else:
    print("Il y a une erreur quelque part. Le code d'erreur est : ", response.status_code)

# créer une application wxPython
app = wx.App()

# créer une fenêtre principale
frame = wx.Frame(None, title="Données récupérées")

# créer un tableau wxPython
table = wx.grid.Grid(frame)

# définir le nombre de lignes et de colonnes pour le tableau
table.CreateGrid(len(data), 1)

# remplir le tableau avec les données
for i, item in enumerate(data):
    table.SetCellValue(i, 0, item)

# afficher la fenêtre principale
frame.Show()

# lancer l'application wxPython
app.MainLoop()
