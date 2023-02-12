import sys
from PyQt5 import QtWidgets, QtGui
from bs4 import BeautifulSoup
import requests


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Scrapping Example")
        self.setGeometry(50, 50, 500, 500)

        self.table = QtWidgets.QTableWidget(self)
        self.table.setRowCount(10)
        self.table.setColumnCount(3)
        self.table.setGeometry(20, 20, 450, 450)

        self.get_data()

    def get_data(self):
        """Methode format string"""
        brand = "BMW"
        year_min = 2010
        year_max = 2019
        url = """https://www.lacentrale.fr/listing?makesModelsCommercialNames={brand}&yearMax={year_max}&yearMin={year_min}""".format(
           brand=brand, year_min=year_min, year_max=year_max)

        # Faire une demande GET à l'URL
        response = requests.get(url)

        # Vérifier que la demande a été réussie
        if response.status_code == 200:
            # Créer un objet BeautifulSoup à partir de la réponse HTML
            soup = BeautifulSoup(response.text, 'html.parser')

            # Trouver tous les éléments searchCard
            search_card_elements = soup.find_all(class_='searchCard')

            # Imprimer le texte de chaque searchCard
            for i, search_card in enumerate(search_card_elements):
                self.table.setItem(i, 0, QtWidgets.QTableWidgetItem(search_card.text))
        else:
            print("Il y a une erreur quelque part. Le code est erreur est : ",
                  response.status_code)


app = QtWidgets.QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
